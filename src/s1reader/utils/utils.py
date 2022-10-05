#!/usr/bin/env python3
# Author: Zhang Yunjun, Feb 2022
# Recommend usage:
#   from s1reader.utils import utils as s1utils


import os
from osgeo import gdal


def write_isce2_meta_file(fname, ds_shape):
    """Write VRT/XML metadata files in ISCE-2 format."""
    # VRT file
    length, width = ds_shape
    line_off = width * 4
    vrt_str = f"""<VRTDataset rasterXSize="{width}" rasterYSize="{length}">
    <VRTRasterBand dataType="Float32" band="1" subClass="VRTRawRasterBand">
        <SourceFilename relativeToVRT="1">{os.path.basename(fname)}</SourceFilename>
        <ByteOrder>LSB</ByteOrder>
        <ImageOffset>0</ImageOffset>
        <PixelOffset>4</PixelOffset>
        <LineOffset>{line_off}</LineOffset>
    </VRTRasterBand>
</VRTDataset>"""

    with open(f'{fname}.vrt', 'w') as fid:
        fid.write(vrt_str)

    # XML file
    ds = gdal.Open(f'{fname}.vrt', gdal.GA_ReadOnly)
    gdal.Translate(fname, ds, format='ISCE')
    return


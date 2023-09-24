import rasterio
from rasterio.features import rasterize
import pathlib

import pandas as pd
import geopandas as gpd
from shapely.geometry import mapping, Point, Polygon
from shapely.ops import cascaded_union, unary_union

import numpy as np
#import cv2
import json
import matplotlib.pyplot as plt

import tifffile as tiff
import folium
import shapely
from PIL import Image

import gdown
import shutil
from xml.dom import minidom
from pystac_client import Client
from glob import glob
import warnings
warnings.filterwarnings('ignore', 'GeoSeries.notna', UserWarning)

# Download files (change download to True to download)
download = False

data_folder = pathlib.Path.cwd().parents[1] / 'Users/butler/Documents/hp/Ladakh/code'
download_path = data_folder / 'Users/butler/Documents/hp/Ladakh/code/Copy_of_1977_1994_2009'
download_path.mkdir(parents=True, exist_ok=True)

(download_path / ".gitignore").write_text("*")

if download:
    gdown.download_folder(id="1vgM5rHjIyN2gd3DoVT_KzRZwvbGZ93cS", quiet=False, use_cookies=False, output=str(download_path))
    print("Remember to change the download option to False")

# Unpack and organize in folders
years = [2009]
for year in years:
    year_folder = '/Users/butler/Documents/hp/Ladakh/code/Copy of 1977_1994_2009/2009'

    if year != 2019:
        # Unpack tar files into their own folder
        tar_files = glob("/Users/butler/Documents/hp/Ladakh/code/Copy of 1977_1994_2009/2009/*.tar")
        for f in tar_files:
            new_dir = download_path / str(year) / f.stem
            new_dir.mkdir(exist_ok=True)
            shutil.unpack_archive(f, extract_dir=new_dir)
            f.unlink()
    else:
        # Group files into the correct folders
        metadata_files = year_folder.glob("*_MTL.xml")
        file_prefixes = [f.stem[:40] for f in metadata_files]

        for prefix in file_prefixes:
            scene_dir = year_folder / prefix

            if not scene_dir.is_dir():
                # TODO: Maybe continue if dir already exists
                scene_dir.mkdir()
            
            scene_files = year_folder.glob(f"{prefix}*")
            for f in scene_files:
                if f.is_file():
                    f.rename(scene_dir / f.name)



shapefile_path = pathlib.Path.cwd().parents[1]/'Users/butler/Documents/hp/Ladakh/code/DATA IN SHAPEFILE FORMAT/GLACIER_OUTLINES/'
#shapefile_crs = gpd.read_file(next(iter(shapefile_path.glob("*_1997.shp")))).crs
files = glob('Users/butler/Documents/hp/Ladakh/code/DATA IN SHAPEFILE FORMAT/GLACIER_OUTLINES/*_1997.shp')

gdfs = gpd.read_file(files)
shapefile_crs = gdfs.crs
#  Load shapefiles
years = [2009]
shapes = {
    year: gpd.GeoDataFrame(pd.concat([gpd.read_file(f) for f in shapefile_path.glob(f"*_{year}.shp")]), crs=shapefile_crs).set_index("JNUOAId", verify_integrity=True)
    for year in years
}

#  Connect to the stac server
stac_url = "https://landsatlook.usgs.gov/stac-server"
cat = Client.open(stac_url)
collection_id = "landsat-c2l1"

#  Create folder for masks
masks_folder = year_folder.parent / "masks"
masks_folder.mkdir(exist_ok=True)


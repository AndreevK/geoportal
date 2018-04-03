import os
from django.contrib.gis.utils import LayerMapping
from .models import Tifs_data

tifs_data_mapping = {
    'fid' : 'fid',
    'location' : 'location',
    'ingestion' : 'ingestion',
    'elevation' : 'elevation',
    'geom' : 'MULTIPOLYGON',
 }

tifs_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tifs_data.shp'))

def run(verbose=True):
 	lm = LayerMapping(Tifs_data, tifs_shp, tifs_data_mapping, transform= False, encoding='iso-8859-1')
 	lm.save(strict=True,verbose=verbose)

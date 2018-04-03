# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Incidences(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = models.GeoManager()

	def __unicode__(self):
		return self.name

class RasterData(models.Model):
    fid = models.AutoField(primary_key=True)
    the_geom = models.PolygonField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    ingestion = models.DateTimeField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geoportal'


    def __unicode__(self):
    	return self.location






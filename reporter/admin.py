# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Incidences, RasterData
# from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	# pass
	list_display =('name', 'location')

class RastersAdmin(LeafletGeoAdmin):
	# pass
	list_display =('location', 'ingestion')



admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(RasterData, RastersAdmin)
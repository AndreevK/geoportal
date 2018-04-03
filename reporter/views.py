# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from models import RasterData
from models import Incidences
import json
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'
	
class JoraFronend33(TemplateView):
	template_name = 'agricom_2.html'

def raster_datasets(request):
	if request.method == 'GET':
		starttime = request.GET.get('starttime')
		endtime =  request.GET.get('endtime')
		if starttime is None:
			queryset = serialize('geojson', RasterData.objects.all())
		else:
			queryset = serialize('geojson', RasterData.objects.filter(ingestion__gte=starttime, ingestion__lte=endtime))
	return HttpResponse(queryset, content_type='json')

def incidences_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points, content_type='json')

# def raster_datasets_by_date(request):
#     if request.method == 'GET':
# 		starttime = request.GET['starttime']
# 		if starttime is None:
# 			queryset = serialize('geojson', RasterData.objects.all())
# 		else:
# 			queryset = serialize('geojson', RasterData.objects.filter(ingestion__lte=starttime))
# 			# response = list(queryset.values("fid", "the_geom", "location", "ingestion", "elevation"))
# 		return HttpResponse(queryset, content_type='json')


    	# y = datetime('2018-03-23')
    	# x = RasterData.objects.filter(ingestion__gte=start)
    	# muravej = serialize('geojson', x)

    	# # startjson = x[-9:]
     #    return HttpResponse(muravej, content_type="json")

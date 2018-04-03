from django.conf.urls import include,url

from views import HomePageView, raster_datasets, incidences_datasets, JoraFronend33



urlpatterns= [
	# url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^$', JoraFronend33.as_view(), name = 'home'),
	url(r'^rasters_data/$', raster_datasets, name = 'rasters'),
	# url(r'^rasters_data_by_date/$', raster_datasets_by_date, name = 'rasters_by_date'),
	# url(r'^rasters_data/(?P<id_num>\d+)/$', raster_datasets, name='time'),
	url(r'incidences_data/', incidences_datasets, name = 'incidence'),
]

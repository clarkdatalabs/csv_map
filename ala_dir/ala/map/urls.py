from django.conf.urls import patterns, url

from . import views

urlpatterns = [
	url(r'^geojson/$', views.geojson, name='geojson'),
	url(r'^csv/$', views.csv, name='csv'),
    url(r'^$', views.index, name='index'),
]
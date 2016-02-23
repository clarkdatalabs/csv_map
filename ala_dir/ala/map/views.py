from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
import csv

from .models import (DataSet, QuantitativeVariable, QuantitativeVariable, Category, Breakpoint)

#def index(request):
    #template =loader.get_template('map/map.html')
    #context = RequestContext(request)
    #return HttpResponse(template.render(context))

def index(request):
	data = DataSet.objects.all()
	template = loader.get_template('map/map.html')
	context = RequestContext(request, {
		'data': data,
		})
	return HttpResponse(template.render(context))
	#return render(request, 'map/map.html')

def geojson(request):
	return render(request,'map/units.json')

def csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename = "data.csv"'

	csv_data = loader.get_template('media/{{DataSet.csv}}')

	t = loader.get_template('map/data_template.txt')
	c = RequestContext(request, {
		'data': csv_data
	})
	response.write(t.render(c))
	return response
	

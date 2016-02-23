from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader

from .models import (DataSet, QuantitativeVariable, QuantitativeVariable, Category, Breakpoint)

#def index(request):
    #template =loader.get_template('map/map.html')
    #context = RequestContext(request)
    #return HttpResponse(template.render(context))

def index(request):
	data = DataSet.objects.all()
	return render(request, 'map/map.html')

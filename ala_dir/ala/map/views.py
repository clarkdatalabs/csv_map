from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.forms.models import model_to_dict
from django.core import serializers
import json

from django.db.models import Max

#from django.utils.functional import Promise
#from django.utils.encoding import force_text
#from django.core.serializers.json import DjangoJSONEncoder


from .models import (DataSet, QuantitativeVariable, QualitativeVariable, Category, Breakpoint)

#def index(request):
    #template =loader.get_template('map/map.html')
    #context = RequestContext(request)
    #return HttpResponse(template.render(context))

def index(request):
	data = DataSet.objects.all()
	template = loader.get_template('map/map.html')
	#json = serializers.serialize('json', DataSet.objects.all())
	context = RequestContext(request, {
		'data': data,
		#'json': json,
		})
	return HttpResponse(template.render(context))
	#return render(request, 'map/map.html')

def geojson(request):
	return render(request,'map/units.json')

def jstr(request):
	# get dataset names and filenames for csv's as strings	
	datasets = DataSet.objects.values()
	# construct a list of dictionaries
	lst = []
	for dataset in datasets:
		dct = {}
		dct2 = {}
		dct['name'] = dataset['name']
		dct['file'] = dataset['csv']
		dct['variables'] = dct2
		# get names of qualitative and quantitative variables as strings
		quant_vars = QuantitativeVariable.objects.values()
		qual_vars = QualitativeVariable.objects.values()
		# associate quantitative variables with appropriate datasets
		for quant_var in quant_vars:
			if dataset['id'] == quant_var['dataset_id']:
				dct2['name'] = quant_var['name'] 
				dct2['type'] = 'quant'
				dct2['color_function'] = 'colorer'
		# associate qualitative variables with appropriate datasets
		for qual_var in qual_vars:
			if dataset['id'] == qual_var['dataset_id']:
				dct2['name'] = qual_var['name'] 
				dct2['type'] = 'qual' 
				dct2['color_function'] = 'colorer'
		lst.append(dct)
		#jstr = json.dumps(lst)
	#return HttpResponse(jstr)
	return JsonResponse(lst, safe=False)	

#class LazyEncoder(DjangoJSONEncoder):
 #   def default(self, obj):
  #      if isinstance(obj, Promise):
   #     	return force_text(obj)
    #    return super(LazyEncoder, self).default(obj)


	

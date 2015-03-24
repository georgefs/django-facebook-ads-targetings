from django.http import HttpResponse
from facebook_ads_targetings import *
from django.utils import simplejson


def index(request):
    return HttpResponse("Hello, world.")

def targetings(request):
    response = {}
    response['types'] = get_types()

    data = simplejson.dumps(response)
    return HttpResponse(data, mimetype='application/json')

def options(request, type_name):
    response = {}
    
    targetings = get_targeting(type_name)
    response['options'] = [ v for v in targetings.options()]
    
    data = simplejson.dumps(response)
    return HttpResponse(data, mimetype='application/json')


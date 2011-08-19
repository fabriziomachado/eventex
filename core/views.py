#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def homepage(request):
    #from django.conf import settings
    #context = {'STATIC_URL': settings.STATIC_URL}
    context = RequestContext(request)
    
    return render_to_response('index.html', context)


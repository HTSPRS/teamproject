from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request) :
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render(None, request))
    return render(request, 'index.html')
# Create your views here.

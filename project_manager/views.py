# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect

def index(request):
    return HttpResponse("Hello World!")

def project(request):
    d={'color':'red',
       'height': 'tall',
       'width': 'wide'}
    return render_to_response('project_manager/project.html', {'description':d, 'name':'Brett', 'age': '35'})


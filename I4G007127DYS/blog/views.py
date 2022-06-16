from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def blog_index(request):
    # ...
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>This the blog index</h1>')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    #return HttpResponse("Hello, world! This is our first view.")
    return HttpResponseRedirect('/bostonunderwater/')

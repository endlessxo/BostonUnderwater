from django.http import HttpResponse
from bostonunderwater.models import Totem
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.contrib import messages
from .forms import ContactForm

def index(request):
    totem_list = Totem.objects.order_by('-latitude')
    output = ', '.join([p.place for p in totem_list])
   # return HttpResponse(output)
    return render(request, 'bostonunderwater/index.html')

def home(request):
    return render(request, 'bostonunderwater/home.html')

def data(request):
    return render(request, 'bostonunderwater/map.html')

def contact(request):
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    return render(request, 'bostonunderwater/contact.html')

def geojson(request):
    return render(request, 'bostonunderwater/geojson.html')

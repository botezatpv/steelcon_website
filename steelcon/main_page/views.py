from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Service, Items

def index(request):
    show_services = Service.objects.order_by('-service_name')[:5]
    output = ', '.join([q.service_name for q in show_services])
    return HttpResponse(output)

def service(request, service_name):
    return HttpResponse("You are looking at service name %s." % 
                        service_name)

def items(request,service_name, item_name):
    return HttpResponse("You are looking at item name %s." %
                        item_name)	
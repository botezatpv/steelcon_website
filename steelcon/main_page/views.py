from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Items
from django.template import loader
# Create your views here.
def index(request):
    show_services = Service.objects.order_by('-service_name')[:5]
    template = loader.get_template('main_page/index.html')
    context = {
        'show_services': show_services,
    }
    return render(request, 'main_page/index.html', context)

def service(request, service_name):
    return HttpResponse("You are looking at service name %s." % 
                        service_name)

def items(request,service_name, item_name):
    return HttpResponse("You are looking at item name %s." %
                        item_name)	
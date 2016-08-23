from django.contrib import admin

# Register your models here.
from .models import Service, Items

admin.site.register(Service)
admin.site.register(Items)


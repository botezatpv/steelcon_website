#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Service, Items

# Register your models here.
class ItemsInline(admin.TabularInline):
    model = Items
    extra  = 1
    
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Название услуги', {'fields': ['service_name']}), 
        ('Описание услуги', {'fields': ['service_description']}), 
        ('Изображение услуги', {'fields': ['service_image']}),
        ]
    inlines = [ItemsInline]
    list_display = ('service_name', 'service_description')
    

admin.site.register(Service, ServiceAdmin)



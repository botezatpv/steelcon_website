from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
# Create your models here.

# Class for adding services.
@python_2_unicode_compatible
class Service(models.Model):
    service_name = models.CharField(max_length = 300)
    service_description = models.CharField(max_length = 3000)
    service_image = models.ImageField(upload_to = r'uploaded_images/Service/', max_length = 100)
    
    def __str__(self):
        return self.service_name

# Class for adding items in services. For each service
# can be added many items. 
@python_2_unicode_compatible
class Items(models.Model):
    item_service = models.ForeignKey(Service)
    item_name = models.CharField(max_length = 300)
    item_description = models.CharField(max_length = 3000)
    item_image = models.ImageField(upload_to = r'uploaded_images/Items/', max_length = 100)
    
    def __str__(self):
        return self.item_name
    
 
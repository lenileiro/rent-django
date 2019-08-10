from django.db import models
import uuid
import os

def get_image_path(instance, filename):
    return os.path.join('photos', "residence_%s" % str(instance.id), filename)
# Create your models here.


class Property(models.Model):
    property_id     = models.AutoField(primary_key=True)
    property_name   = models.CharField(max_length=255)
    address         = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    county          = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class PropertyFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture   = models.ImageField(upload_to=get_image_path, blank=True)
    feed      = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='files')
    

class Unit(models.Model):
    unit_number     = models.CharField(max_length=255)
    property_id     = models.ForeignKey(Property, on_delete=models.CASCADE)
    floor           = models.IntegerField()
    bedrooms        = models.IntegerField()
    bathrooms       = models.IntegerField()
    status          = models.CharField(max_length=10)

    def __str__(self):
        return str(self.unit_number)

class Tenant(models.Model):
    tenant_id      = models.IntegerField()
    first_name     = models.CharField(max_length=100)
    last_name      = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name)
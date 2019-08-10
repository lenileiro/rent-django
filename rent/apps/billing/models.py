from django.db import models

from rent.apps.property.models import Unit, Property, Tenant
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/property/2019/08/01/<filename>
    return 'recient/%Y/%m/%d/{0}/'.format(filename)

class Lease(models.Model):
    lease_id        = models.IntegerField()
    property_id     = models.ForeignKey(Property, on_delete=models.CASCADE) 
    unit_id         = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    tenant_id       = models.ForeignKey(Tenant, on_delete=models.CASCADE) 
    start_date      = models.DateTimeField(auto_now_add=True)
    end_date        = models.DateTimeField()
    active          = models.CharField(max_length=3)
    rent            = models.IntegerField()

    def __str__(self):
        return str(self.lease_id)

class Payment(models.Model):
    expense_id      = models.IntegerField()
    property_id     = models.ForeignKey(Property, on_delete=models.CASCADE) 
    unit_id         = models.ForeignKey(Unit, on_delete=models.CASCADE) 
    tenant_id       = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    expense_type    = models.CharField(max_length=255)
    cost            = models.IntegerField()
    date            = models.DateTimeField(auto_now_add=True)
    recient         = models.FileField(upload_to=user_directory_path)
    is_paid         = models.BooleanField(default=False)

    def __str__(self):
        return str(self.expense_id)
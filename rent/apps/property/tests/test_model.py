import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib import auth
from django.test import TestCase, Client
from ..models import Unit, Property, Tenant, PropertyFile

# Create your tests here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestPropertyModel(TestCase):
    def setUp(self):
        self.permanent_address = Property.objects.create(
            property_name="central court",
            address="255 Nairobi, Kenya",
            city="Nairobi",
            county="Nairobi")

    def test_create_property(self):

        for i in range(1, 5):
            file = os.path.join(BASE_DIR, f'tests/media/{i}.jpg')
            with open(file, 'rb') as file:
                document = SimpleUploadedFile(
                    file.name, file.read(), content_type='image/*')

                PropertyFile.objects.create(feed=self.permanent_address, picture=document)

class TestUnitModel(TestCase):
    def setUp(self):
        self.permanent_address = Property.objects.create(
            property_name="central court",
            address="255 Nairobi, Kenya",
            city="Nairobi",
            county="Nairobi")

    def test_create_unit(self):
        Unit.objects.create(
            unit_number="unit_001", 
            property_id=self.permanent_address,
            floor=1,
            bedrooms=3,
            bathrooms=3,
            status="VACANT"
            )
        unit = Unit.objects.filter(unit_number="unit_001")[0]
        self.assertEqual(unit.get_unit_number, "unit_001")

class TestTenantModel(TestCase):
    def test_register_tenant(self):
        Tenant.objects.create(
            tenant_id= int("00001"),
            first_name= "sam",
            last_name ="paul"
        )
        tenant = Tenant.objects.filter(tenant_id= int("00001"))[0]
        self.assertEqual(tenant.get_first_name, "sam")

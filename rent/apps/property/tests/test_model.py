import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib import auth
from django.test import TestCase, Client
from ..models import Unit, Property, Tenant, PropertyFile

# Create your tests here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestPropertyModel(TestCase):

    def test_create_property(self):
        self.permanent_address = Property.objects.create(
                property_name="central court",
                address="255 Nairobi, Kenya",
                city="Nairobi",
                county="Nairobi")

        for i in range(1, 5):
            file = os.path.join(BASE_DIR, f'tests/media/{i}.jpg')
            with open(file, 'rb') as file:
                document = SimpleUploadedFile(
                    file.name, file.read(), content_type='image/*')

                PropertyFile.objects.create(feed=self.permanent_address, picture=document)
        
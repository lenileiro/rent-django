from django.test import TestCase
from django.contrib import auth
from django.test import TestCase, Client
from ..models import User

# Create your tests here.
class AuthTestVendorUser(TestCase):

    def setUp(self):
        """ Defining test variables """
        self.client = Client()
        self.user = User.objects.create_vendoruser(
            name='anthony',
            email='email@email.com',
            password='asdfghjkl',
            phone="+254729363838",
            contactperson="sam"
            )
        self.user.save()

    
    def test_Login(self):
        self.assertEqual(self.user.is_Vendor, True)
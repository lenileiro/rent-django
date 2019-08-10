from django.test import TestCase
from django.contrib import auth
from django.test import TestCase, Client
from ..models import User

# Create your tests here.

class AuthTestBasicUserOperation(TestCase):

    def test_required_field_name(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_user(
            email='email@email.com',
            password='my_password',
            )
            self.user.save()
          
        self.assertEqual(
            str(context.exception), "User must have a name.")

    def test_required_field_email(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_user(
            name='anthony',
            password='my_password',
            )
            self.user.save()
            
        self.assertEqual(
            str(context.exception), "User must have an email address.")
    
    def test_required_field_password(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_user(
                name='anthony',
                email='email@email.com',
                )
            self.user.save()
            
        self.assertEqual(
            str(context.exception), "User Account must have a password.")


    def test_invalid_email_format(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_user(
            name='anthony',
            email='email@emailcom',
            password='my_password',
            )
            self.user.save()
          
        self.assertEqual(
            str(context.exception), "Incorrect email format please try again")
    
    def test_used_email(self):
        self.user1 = User.objects.create_user(
            name='anthony',
            email='email@email.com',
            password='my_password',
            )
        self.user1.save()

        with self.assertRaises(TypeError) as context:
            self.user2 = User.objects.create_user(
            name='anthony',
            email='email@email.com',
            password='my_password',
            )
            self.user2.save()
            
        self.assertEqual(
            str(context.exception), "This email has already been used to create a user")

class AuthTestSuperUser(TestCase):

    def test_create_superuser(self):
        self.user = User.objects.create_superuser(
            name='anthony',
            email='email@email.com',
            password='my_password'
            )
        self.user.save()

        self.assertEqual(self.user.is_SuperUser, True)

class AuthTestOwnerUser(TestCase):

    def test_create_owneruser(self):
        self.user = User.objects.create_owneruser(
            name='anthony',
            email='email@email.com',
            password='my_password'
            )
        self.user.save()
        self.assertEqual(self.user.is_Owner, True)

class AuthTestVendorUser(TestCase):
    
    def test_create_vendoruser(self):
        self.user = User.objects.create_vendoruser(
            name='anthony',
            email='email@email.com',
            password='my_password',
            phone="+254729363838",
            contactperson="sam"
            )
        self.user.save()
        self.assertEqual(self.user.is_Vendor, True)

    def test_required_field_phone(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_vendoruser(
                name='anthony',
                email='email@email.com',
                password='my_password',
                contactperson="sam"
                )
            self.user.save()
            
        self.assertEqual(
            str(context.exception), "Vendor Account must have a phone number.")

    def test_required_field_contactperson(self):
        with self.assertRaises(TypeError) as context:
            self.user = User.objects.create_vendoruser(
                name='anthony',
                email='email@email.com',
                password='my_password',
                phone="+254729363838"
                )
            self.user.save()
            
        self.assertEqual(
            str(context.exception), "Vendor Account must have a contactperson.")
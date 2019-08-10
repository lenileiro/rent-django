import re
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, name=None, email=None, password=None):
        """Create and return a `User` with an email, username and password."""
        if name is None:
            raise TypeError('User must have a name.')

        if email is None:
            raise TypeError('User must have an email address.')

        if password is None:
            raise TypeError('User Account must have a password.')

        Utils.validate_email(email)

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


    
    def create_superuser(self, name, email, password):
        if password is None:
            raise TypeError('Superuser must have a password.')

        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_owneruser(self, name, email, password):

        user = self.create_user(name, email, password)
        user.is_owner = True
        user.save()

        return user
    
    def create_vendoruser(self, name, email, password, phone=None, contactperson=None):
        if phone is None:
            raise TypeError('Vendor Account must have a phone number.')
        if contactperson is None:
            raise TypeError('Vendor Account must have a contactperson.')
         
        user = self.create_user(name, email, password)
        user.is_vendor = True
        user.phone = phone
        user.contactperson = contactperson
        user.save()

        return user

   

class User(AbstractBaseUser, PermissionsMixin):
    name            = models.CharField(max_length=255)
    email           = models.EmailField(db_index=True, unique=True)
    is_active       = models.BooleanField(default=True)
    is_vendor       = models.BooleanField(default=False)
    is_owner        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    phone           = models.CharField(default=False, max_length=255)
    contactperson   = models.CharField(default=False, max_length=255)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['name']
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    @property
    def is_SuperUser(self):
        return self.is_superuser

    @property
    def is_Owner(self):
        return self.is_owner

    @property
    def is_Vendor(self):
        return self.is_vendor
    

class Utils:
    @staticmethod
    def validate_email(email):
        check_email = User.objects.filter(email=email)
        email_regex = r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$'
        if not re.search(email_regex, email):
            raise TypeError("Incorrect email format please try again")
        if check_email.exists():
            raise TypeError("This email has already been used to create a user")
        return email

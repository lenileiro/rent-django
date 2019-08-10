import re
from django.contrib import auth
from .models import User

class Validator:
    @staticmethod
    def validate_email(email):
        check_email = User.objects.filter(email=email)
        email_regex = r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$'
        if not re.search(email_regex, email):
            raise TypeError("Incorrect email format please try again")
        if check_email.exists():
            raise TypeError("This email has already been used to create a user")
        return email
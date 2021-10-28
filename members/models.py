from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UsernameField
from django.db import models


# class User(AbstractUser):
#     username = models.CharField(max_length=50, error_messages={'required': 'this field is required!', 'blank': 'this field can not be blank!'})
#     password = models.CharField(max_length=50, error_messages={'required': 'this field is required!', 'blank': 'this field can not be blank!'})
#     USERNAME_FIELD = 'username'

    
# class Register(models.Model):
#     username = models.CharField(max_length=50, unique=True, error_messages=login_errors_mess)
#     password = models.CharField(max_length=50, error_messages=password_errors_mess)
#     def __str__(self):
#         return self.name
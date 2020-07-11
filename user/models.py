from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length = 10, unique = True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    phone = models.CharField(max_length = 13, unique = True)
    email = models.EmailField(unique = True, blank = True)
    password = models.CharField(max_length = 20)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [ 'first_name', 'last_name','phone','email', 'password']
# Create your models here.
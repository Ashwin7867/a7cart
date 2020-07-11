from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length = 30, unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 13, unique = True)
    email = models.EmailField(unique = True, blank = True)
    password = models.CharField(max_length = 200)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [ 'first_name', 'last_name','phone','email', 'password']
# Create your models here.

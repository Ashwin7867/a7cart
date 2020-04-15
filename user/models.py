from django.db import models
from oscar.apps.customer.abstract_models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length = 20, blank = True, null = True)
    phone = models.CharField( blank = True, null =True, max_length = 12)

# Create your models here.

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Donor(models.Model):
    name = models.CharField(max_length=75)
    
   #phone_num = PhoneNumberField(null=False, blank=False, unique=True)
    

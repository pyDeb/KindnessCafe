from django.db import models

# Create your models here.

class Homepage(models.Model):
    text_body = models.TextField()
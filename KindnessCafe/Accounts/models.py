from django.db import models

# Create your models here.

class News(models.Model):
    #feilds
    title = models.CharField(max_length=75, blank=False)
    desc = models.TextField(blank=True)
    image = models.ImageField()
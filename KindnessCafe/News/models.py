from django.db import models


# Create your models here.
class News(models.Model):
    #feilds
    title = models.CharField(max_length=75, blank=False)
    desc = models.TextField(blank=True)
    image_1 = models.ImageField(blank=True, upload_to='uploaded_images')
    alt_1 = models.CharField(max_length=400, blank=True)

    image_2 = models.ImageField(blank=True)
    alt_2 = models.CharField(max_length=400, blank=True)

    image_3 = models.ImageField(blank=True)
    alt_3 = models.CharField(max_length=400, blank=True)

    image_4 = models.ImageField(blank=True)
    alt_4 = models.CharField(max_length=400, blank=True)

    published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)



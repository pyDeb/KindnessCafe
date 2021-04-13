from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    #feilds
    title = models.CharField(max_length=75, blank=False)
    desc = RichTextField()

    TAG_CATEGORY = [
        ('NEWS', 'NEWS'),
        ('EVENT', 'EVENT'),
        ('LIVE', 'LIVE'),
        ('OTHER', 'OTHER'),
    ]

    tag = models.CharField(choices=TAG_CATEGORY, max_length=5,  default='NEWS')

    image_1 = models.ImageField(blank=True)
    alt_1 = models.CharField(max_length=400, blank=True)

    image_2 = models.ImageField(blank=True)
    alt_2 = models.CharField(max_length=400, blank=True)

    image_3 = models.ImageField(blank=True)
    alt_3 = models.CharField(max_length=400, blank=True)

    image_4 = models.ImageField(blank=True)
    alt_4 = models.CharField(max_length=400, blank=True)

    published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

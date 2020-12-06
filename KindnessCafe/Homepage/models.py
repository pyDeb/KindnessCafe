from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Homepage(models.Model):
    text_body = RichTextField()
from django.db import models
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Homepage(models.Model):
    text_body = RichTextField()
    title = models.TextField(default="A new KindnessCafe news!")


    def __str__(self):
        return self.title

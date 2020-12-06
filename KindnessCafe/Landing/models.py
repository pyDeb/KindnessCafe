from django.db import models


# Create your models here.
class LandingContent(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name="Title of landing section of the Home page")
    description = models.TextField(blank=False, verbose_name="Paragraph of the landing section of the Home page")

    def __str__(self):
        return self.title

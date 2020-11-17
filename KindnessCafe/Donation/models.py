from django.db import models

# Create your models here.

class Donation(models.Model):
    d_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75, default="Anonymous")
    amount = models.FloatField()
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

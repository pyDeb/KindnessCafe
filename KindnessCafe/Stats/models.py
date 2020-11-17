from django.db import models

# Create your models here.
class StatItem(models.Model):
    icon = models.FileField()
    title = models.CharField(max_length = 24, verbose_name = "Title of the the stat limited to 24 Character")
    data_min = models.IntegerField(default=0, blank=True, verbose_name="Starting Value")
    data_max = models.IntegerField(verbose_name="Reaching Value")
    data_delay = models.IntegerField(default=2, blank=True, verbose_name="Total Animation Time")
    data_increment = models.IntegerField(default=1, blank=True, verbose_name="Incrementor step")
    units_field = models.CharField(max_length = 3, blank = True)


    def __str__(self):
        return self.title + ' (' + str(self.data_max) + ')'
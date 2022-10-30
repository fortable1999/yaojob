from django.db import models

# Create your models here.


class YaoJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

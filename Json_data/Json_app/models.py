from django.db import models

# Create your models here.

class Timeslat(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()

class Customer(models.Model):
    id_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    time = models.ManyToManyField(Timeslat)

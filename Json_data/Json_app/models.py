from django.db import models


class Timeslat(models.Model):

    startdate = models.DateTimeField(default='Asia/Kolkata')
    enddate = models.DateTimeField(default='Asia/Kolkata')


class Customer(models.Model):
    id_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    time = models.ManyToManyField(Timeslat)

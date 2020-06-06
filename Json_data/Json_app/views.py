from django.shortcuts import render
from .serializer import Timeslat_Serializer,Customer_Serializer
from rest_framework.viewsets import ModelViewSet
from .models import Timeslat,Customer
from rest_framework.views import APIView
from rest_framework.response import Response

class Time_slat_post(ModelViewSet):
    queryset = Timeslat.objects.all()
    serializer_class = Timeslat_Serializer


class Customer_post(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer






from django.shortcuts import render
from .serializer import Timeslat_Serializer,Customer_Serializer
from rest_framework.viewsets import ModelViewSet
from .models import Timeslat,Customer
from rest_framework.views import APIView
from rest_framework.response import Response

class Time_slat_post(ModelViewSet):
    queryset = Timeslat.objects.all()
    serializer_class = Timeslat_Serializer


# class Customer_post(ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = Customer_Serializer

class Customer_post(APIView):
    def post(self,request):
        data = request.data
        scr = Customer_Serializer(data=data)
        if scr.is_valid():
            b=scr.save()
            time = request.data['time']
            for x in time:
                a=Timeslat.objects.get(id=x)
                b.time.add(a)
        return Response(scr.data)

    def get(self,request):
        qs = Customer.objects.all()
        scr = Customer_Serializer(qs,many=True)
        return Response(scr.data)








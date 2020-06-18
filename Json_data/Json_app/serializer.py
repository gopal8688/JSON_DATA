from rest_framework import serializers
from .models import Timeslat, Customer


class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id_no', 'name', 'time']
        depth = 1


class Timeslat_Serializer(serializers.ModelSerializer):
    # cust = Customer_Serializer(read_only=True)
    class Meta:
        model = Timeslat
        fields = ['startdate' 'enddate']
        # exclude = ['id']
        # depth = 1

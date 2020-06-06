from rest_framework import serializers
from .models import Timeslat, Customer





class Customer_Serializer(serializers.ModelSerializer):
    #time = serializers.PrimaryKeyRelatedField(read_only=True)
    #time = Timeslat_Serializer(many=True)
    class Meta:
        model = Customer
        fields = ['id_no','name','time']
        depth=1


class Timeslat_Serializer(serializers.ModelSerializer):
    #time=Customer_Serializer(many=True)
    class Meta:
        model = Timeslat
        fields = '__all__'
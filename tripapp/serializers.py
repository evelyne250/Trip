from rest_framework import serializers
from .models import *
class Merch1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ('name', 'permit', 'tel','user_id','platenbr')

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'Time','phone','currentLocation','destination')

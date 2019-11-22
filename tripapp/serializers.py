from rest_framework import serializers
from .models import Client
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'Time','phone','currentLocation','destination')

from rest_framework import serializers
from .models import *
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ('name', 'permit', 'tel','user_id','platenbr')

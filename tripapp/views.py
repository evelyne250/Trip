from django.shortcuts import render
from pyrebase import pyrebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Entries
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MerchSerializer
from rest_framework import status
# Create your views here.

config = {
  'apiKey': "AIzaSyDHi4Xa5mRRl4Rurv1AwIavg8BBMYEwxaU",
  'authDomain': "trip-78226.firebaseapp.com",
  'databaseURL': "https://trip-78226.firebaseio.com",
  'projectId': "trip-78226",
  'storageBucket': "trip-78226.appspot.com",
  'messagingSenderId': "1054259298007",
  'appId': "1:1054259298007:web:450dceb3a72d1520ac3a92",
  'measurementId': "G-PCF3CV3GFT"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
@login_required(login_url='/accounts/login/')
def signIn(request):
    drivers= Entries.objects.all()
    return render(request, "signIn.html",{"drivers": drivers})

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Entries.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

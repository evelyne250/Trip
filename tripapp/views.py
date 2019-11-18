from django.shortcuts import render
from pyrebase import pyrebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Entries
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

from rest_framework import status
from django.shortcuts import render
from pyrebase import pyrebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from django.contrib.auth.decorators import login_required
# Create your views here.

# from .models import Clients
from django.views import View
from django.views.generic import ListView, DetailView


def welcome(request):
    return render (request, "welcome.html")
@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render (request, "dashboard.html")
def dashboard1(request):
    return render (request, "clients.html")
def dashboard2(request):
    return render (request, "drivers.html")
def signIn(request):
    drivers= Entries.objects.all()
    return render(request, "signIn.html",{"drivers": drivers})



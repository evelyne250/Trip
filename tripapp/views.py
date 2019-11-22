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
# Create your views here.

# from .models import Clients
from django.views import View
from django.views.generic import ListView, DetailView


class SnippetListView(ListView):
    model = Client
    template_name = 'snippets/snippet_list.html'


class SnippetDetailView(DetailView):
    model = Client
    template_name = 'snippets/snippet_detail.html'
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Client.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        # print(all_merch)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def signIn(request):
    drivers= Entries.objects.all()
    return render(request, "signIn.html",{"drivers": drivers})

class MerchList1(APIView):
    def get(self, request, format=None):
        all_merch = Entries.objects.all()
        serializers = Merch1Serializer(all_merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = Merch1Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets

# Create your views here.

class ManagementStoreView(viewsets.ModelViewSet):
    queryset = ManagementStore.objects.all()
    serializer_class = managementStoreSerializer
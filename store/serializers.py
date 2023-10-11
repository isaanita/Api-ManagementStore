from .models import *
from rest_framework import serializers

class managementStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementStore
        fields = ['id', 'name', 'description', 'stock', 'createdAt']
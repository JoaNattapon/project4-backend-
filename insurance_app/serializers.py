from rest_framework import serializers
from .models import Packages, Users

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = ['pack_id', 'description', 'price', 'buydate']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'name', 'address', 'email', 'package']
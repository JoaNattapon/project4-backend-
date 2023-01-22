from rest_framework import serializers
from .models import Packages, Users

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
        #  ['description', 'price', 'buydate',]

class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 150, default= "")
    password = serializers.CharField(max_length = 150, default= "")
    name = serializers.CharField(max_length = 200, default = "")
    address = serializers.CharField(max_length = 500, default = "")
    email = serializers.CharField(max_length = 200, default = "")
    class Meta:
        model = Users
        fields = ['username', 'password', 'name', 'address', 'email', 'package']
        depth = 1


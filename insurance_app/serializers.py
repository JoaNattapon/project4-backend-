from rest_framework import serializers
from .models import Packages, Users

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
        #  ['description', 'price', 'buydate',]

class UsersSerializer(serializers.ModelSerializer):
    # packages = serializers.ModelSerializer(
    #     view_name="package_detail"
    # )
    # package_detail=serializers.PrimaryKeyRelatedField(

    #     source='package',
    #     queryset= Packages.objects.all()
    # )
    # pack=serializers.PrimaryKeyRelatedField(
    #     queryset= Packages.objects.all()
    # )
    class Meta:
        model = Users
        fields = ['username', 'name', 'address', 'email', 'package']
        depth = 1


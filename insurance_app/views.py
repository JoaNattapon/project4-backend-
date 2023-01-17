from django.shortcuts import render
from django.http import JsonResponse
from .models import Packages, Users
from .serializers import PackagesSerializer, UsersSerializer
from rest_framework.decorators import api_view

# Create your views here.

def packages_list(request):

    package = Packages.objects.all()
    serializer = PackagesSerializer(package, many = True)
    return JsonResponse({'packages':serializer.data})









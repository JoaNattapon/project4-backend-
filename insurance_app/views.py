from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Packages, Users
from .serializers import PackagesSerializer, UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.

def packages_list(request):

    package = Packages.objects.all()
    serializer = PackagesSerializer(package, many = True)
    return JsonResponse({'packages':serializer.data})


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return Response({'Message':'Logged In'}, status = status.HTTP_200_OK)
        else:
            return Response({'Message': "Invalid username and password"}, status = status.HTTP_401_UNAUTHORIZED)


class SignupView(APIView):
    def post(self, request):
        data = request.data
        try:
            user = User.objects.create_user(username=data["username"],password=data["password"])
            user.save()
            user_data = Users.objects.create(user=user,name=data["name"],address=data["address"],email=data["email"], username=data["username"])
            user_data.save()
            return Response({'message': 'Account created sucessfully.'},status = status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'message': 'Username already taken.'},status = status.HTTP_400_BAD_REQUEST)

class EditUserView(APIView):
    def put(self, request, id):
        user = Users.objects.get(id=id)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def buy_package(request, package_id):
    if request.method == 'PUT':
        package = get_object_or_404(Packages, pk = package_id)
        user = request.user
        user.package = package
        user.save()
        return JsonResponse({'message': 'Purchase successful'})


def home(request):
    if request.user.is_authenticated:
        print('Yes')
        if request.user.is_staff == False:
            user = request.user
    else :
        print('No')

class LogoutView(APIView):
    permissions_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"success": "Successfully logged out"})









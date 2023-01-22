from insurance_app import views
from django.contrib import admin
from django.urls import path
from .views import SignupView, LoginView, LogoutView
from rest_framework import routers
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    # path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path('users/', views.UsersList.as_view(), name = 'user_list'),
    path('users/<int:pk>', views.UsersDetail.as_view(), name = 'user_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


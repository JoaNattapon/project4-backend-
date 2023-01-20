from django.db import models
from django.conf import settings

# Create your models here.

class Packages(models.Model):
    description = models.CharField(max_length = 500)
    price = models.IntegerField()
    buydate = models.DateField()

    def __str__(self):
        return f'{self.description}'

class Users(models.Model):
    username = models.CharField(max_length = 150, default= "")
    password = models.CharField(max_length = 150, default= "")
    name = models.CharField(max_length = 200, default = "")
    address = models.CharField(max_length = 500, default = "")
    email = models.CharField(max_length = 200, default = "")
    package = models.ForeignKey('insurance_app.Packages', on_delete = models.CASCADE, default = "7")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.username
    
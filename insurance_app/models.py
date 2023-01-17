from django.db import models

# Create your models here.

class Packages(models.Model):
    pack_id = models.AutoField(primary_key = True)
    description = models.CharField(max_length = 500)
    price = models.IntegerField()
    buydate = models.DateField()

    def __str__(self):
        return f'{self.pack_id}'

class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    email = models.CharField(max_length = 200)
    package = models.ForeignKey('insurance_app.Packages', on_delete = models.CASCADE)

    def __str__(self):
        return self.user_id
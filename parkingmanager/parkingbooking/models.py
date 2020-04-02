from django.db import models
from django.forms import ModelForm
from PIL import Image

class ParkingPlace(models.Model):
    code = models.CharField(max_length=200, null=False)

class UserCar(models.Model):
    electric = models.BooleanField(default=False)
    plate = models.CharField(max_length=20, null=True)
    car_image = models.ImageField(upload_to='files/', null=True)

class ParkingUser(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    car = models.ForeignKey(UserCar, on_delete=models.CASCADE, null=True)
    place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, null=True)





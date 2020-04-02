
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm
from .models import ParkingPlace,ParkingUser,UserCar

class ParkingPlaceForm(ModelForm):

    class Meta:
        model = ParkingPlace
        fields = ['code']

class ParkingUserForm(ModelForm):

    class Meta:
        model = ParkingUser
        fields = ['name', 'surname']

class ParkingCarUserForm(ModelForm):

    class Meta:
        model = UserCar
        fields = ['electric','car_image']


class BookingParkingForm(MultiModelForm):
    form_classes = {
        'Place': ParkingPlaceForm,
        'User': ParkingUserForm,
        'Car': ParkingCarUserForm,
    }

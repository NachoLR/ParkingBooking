from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .forms import *
from.Tools.ocr_reader import OcrReader
from .models import *
from django.template import loader


def index(request):

    if request.method == 'GET':
        return render(request, "index.html")

    elif request.method == 'POST':
        print("HERE")
        return render(request, "index.html")

def users(request):
    users_list = ParkingUser.objects.all()
    print(users_list)
    template = loader.get_template('users.html')
    context = {
        'users_list': users_list,
    }
    return HttpResponse(template.render(context, request))



class CreateBookingView(CreateView):

    form_class = BookingParkingForm
    template_name = 'formulario.html'

    def form_valid(self, form):
        place = form['Place'].save()
        car = form['Car'].save(commit=False)
        car.plate = self.get_car_plate_from_image(car.car_image)
        car.save()
        user = form['User'].save(commit=False)
        user.car = car
        user.place = place
        user.save()

        return HttpResponseRedirect("/manage")


    def get_car_plate_from_image(self, image_path):

        return OcrReader().get_text_from_image(image_path)






from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateBookingView.as_view(), name='index'),
    path('manage/', views.users, name='users'),
]
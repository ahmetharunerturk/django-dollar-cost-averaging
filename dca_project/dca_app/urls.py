from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_dca, name='calculate_dca'),
]

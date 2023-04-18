from django.urls import path
from . import views

urlpatterns = [
    path('place_older/', views.place_order, name='place_order')
]

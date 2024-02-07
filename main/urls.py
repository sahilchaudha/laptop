from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index),
    path('laptops/',views.laptops),
    path('contact/',views.contact),
    path('about/',views.about),
    path('base/',views.base),
]



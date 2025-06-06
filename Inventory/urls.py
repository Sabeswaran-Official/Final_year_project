from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('base/',basepage),
    path('contact/',contactpage),
]

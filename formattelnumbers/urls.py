from django.urls import path
from . import views

urlpatterns = [
    path('formattelnumbers/', views.format_tel_numbers_input, name='formattelnumbers'),
]

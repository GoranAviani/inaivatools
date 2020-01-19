from django.urls import path
from . import views

urlpatterns = [
    path('code/', views.text_to_morse, name='texttomorse'),
]

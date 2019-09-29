from django.urls import path
from . import views

urlpatterns = [
    path('splitit/', views.split_text_input, name='splittextinput'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('comparelists/', views.compare_lists, name='comparelists'),
]

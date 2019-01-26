from django.urls import path
from . import views

urlpatterns = [
    path('mergeit/', views.merge_text_input, name='mergetextinput'),
]

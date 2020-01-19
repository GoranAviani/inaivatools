from django.urls import path
from . import views

urlpatterns = [
    path('coderdecoder/', views.morse_coder_decoder, name='morsecodecoderdecoder'),
]

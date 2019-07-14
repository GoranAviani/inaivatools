from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('formattelnumbers/', views.format_tel_numbers_api.as_view(), name='api-formattelnumbers'),

]
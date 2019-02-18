from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('formattelnumbers/', views.format_tel_numbers_input, name='formattelnumbers'),
    path('formattelnumbersupload/', views.format_tel_numbers_upload, name='formattelnumbersupload'),
    path('formattelnumbersuploaddesc/', views.render_formatTelNumbersUpload_description_page, name='FormatTelNumExcelSEtPage'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
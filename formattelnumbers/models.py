from django.db import models

# Create your models here.


class uploaded_documents(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='format_tel_number/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
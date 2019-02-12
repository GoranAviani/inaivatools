from django.db import models

# Create your models here.
from django.core.files.storage import FileSystemStorage
#from django.conf import settings
#import os


class OverwriteStorage(FileSystemStorage):
    '''
    Muda o comportamento padrão do Django e o faz sobrescrever arquivos de
    mesmo nome que foram carregados pelo usuário ao invés de renomeá-los.
    '''
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            #os.remove(os.path.join(settings.MEDIA_ROOT, name))
            self.delete(name)
        return name


class uploaded_documents(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(storage=OverwriteStorage(), upload_to='format_tel_number/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
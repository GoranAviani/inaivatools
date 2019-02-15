from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# users/admin.py
from .models import uploaded_documents

class uploaded_documents_admin(admin.ModelAdmin):
  list_display = ['document','document_user','uploaded_at','description']
  list_filter = ('uploaded_at','description')
  date_hierarchy = 'uploaded_at'

admin.site.register(uploaded_documents, uploaded_documents_admin)
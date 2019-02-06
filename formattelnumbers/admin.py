from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# users/admin.py
from .models import uploaded_documents


#class uploaded_documents_admin(uploaded_documents):
    
   # add_form = custom_user_creation_form
  #  form = custom_user_change_form
#    model = uploaded_documents
   # list_display = ['username','email','mobileNumber','first_name', 'last_name','is_active','is_staff','is_superuser','last_login' ]
  #  fieldsets = (
  #  (None, {'fields': ('username', 'email', 'password')}),
 #  ('Basic info', {'fields': ( 'first_name', 'last_name','birthDate')}),
 #   ('Other info', {'fields': ( 'mobileNumber', 'location')}),
 # ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active','groups')}),
  #      ('Important dates', {'fields': ( 'last_login', 'date_joined')}),
  # )

admin.site.register(uploaded_documents)
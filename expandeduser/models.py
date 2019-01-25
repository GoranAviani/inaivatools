from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    mobileNumber = models.CharField(max_length=50,null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.email
# Generated by Django 2.1.5 on 2019-02-15 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import formattelnumbers.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('formattelnumbers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploaded_documents',
            name='document_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploaded_documents',
            name='document',
            field=models.FileField(storage=formattelnumbers.models.OverwriteStorage(), upload_to='format_tel_number/'),
        ),
    ]
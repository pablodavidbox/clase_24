# Generated by Django 4.1.4 on 2023-03-22 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='imagen_cv',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]

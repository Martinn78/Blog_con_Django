# Generated by Django 5.1 on 2024-08-29 23:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen_portada',
            field=models.ImageField(blank=True, default='image_default.png', null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-27 23:47

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_image23_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image23',
            name='image',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='static/'),
        ),
    ]

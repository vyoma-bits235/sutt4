# Generated by Django 4.2.7 on 2023-12-02 01:11

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_rating_avg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image23',
            name='image',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='myimage'),
        ),
    ]

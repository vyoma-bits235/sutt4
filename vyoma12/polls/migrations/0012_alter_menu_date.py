# Generated by Django 4.2.7 on 2023-11-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_menu_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

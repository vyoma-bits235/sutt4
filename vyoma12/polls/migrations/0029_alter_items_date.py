# Generated by Django 4.2.7 on 2023-12-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_alter_items_item1_alter_items_item10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='date',
            field=models.CharField(default='.', max_length=255),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_alter_items_item1_alter_items_item10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item1',
            field=models.CharField(default='0', max_length=255),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_at2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('breakfast', models.CharField(max_length=350)),
                ('dinner', models.CharField(max_length=350)),
                ('lunch', models.CharField(max_length=350)),
            ],
        ),
    ]

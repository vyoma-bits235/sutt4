# Generated by Django 4.2.7 on 2023-12-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_alter_image23_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('item1', models.CharField(max_length=255)),
                ('item2', models.CharField(max_length=255)),
                ('item3', models.CharField(max_length=255)),
                ('item4', models.CharField(max_length=255)),
                ('item5', models.CharField(max_length=255)),
                ('item6', models.CharField(max_length=255)),
                ('item7', models.CharField(max_length=255)),
                ('item8', models.CharField(max_length=255)),
                ('item9', models.CharField(max_length=255)),
                ('item10', models.CharField(max_length=255)),
                ('item11', models.CharField(max_length=255)),
                ('item12', models.CharField(max_length=255)),
                ('item13', models.CharField(max_length=255)),
                ('item14', models.CharField(max_length=255)),
                ('item15', models.CharField(max_length=255)),
                ('item16', models.CharField(max_length=255)),
                ('item17', models.CharField(max_length=255)),
                ('item18', models.CharField(max_length=255)),
                ('item19', models.CharField(max_length=255)),
                ('item20', models.CharField(max_length=255)),
                ('item21', models.CharField(max_length=255)),
                ('item22', models.CharField(max_length=255)),
                ('item23', models.CharField(max_length=255)),
                ('item24', models.CharField(max_length=255)),
            ],
        ),
    ]
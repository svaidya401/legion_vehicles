# Generated by Django 3.1.3 on 2020-11-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BikeManufacturers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=255)),
                ('ex_showroom_price', models.CharField(blank=True, max_length=100)),
                ('image_link', models.TextField(blank=True)),
                ('engine_displacement', models.CharField(blank=True, max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes_app.bikemanufacturers')),
            ],
        ),
    ]

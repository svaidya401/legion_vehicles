# Generated by Django 3.1.3 on 2020-11-28 13:46

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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, max_length=255)),
                ('ex_showroom_price', models.CharField(blank=True, max_length=100)),
                ('image_link', models.TextField(blank=True)),
                ('engine_displacement', models.CharField(blank=True, max_length=100)),
                ('variant', models.CharField(blank=True, max_length=255)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes_app.bikemanufacturers')),
            ],
        ),
        migrations.CreateModel(
            name='BikeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(blank=True, max_length=255)),
                ('cooling_system', models.CharField(blank=True, max_length=100)),
                ('power', models.CharField(blank=True, max_length=100)),
                ('torque', models.CharField(blank=True, max_length=100)),
                ('fuel_type', models.CharField(blank=True, max_length=50)),
                ('wheels', models.CharField(blank=True, max_length=100)),
                ('transmission', models.CharField(blank=True, max_length=100)),
                ('no_of_gears', models.CharField(blank=True, max_length=100)),
                ('brake_front', models.CharField(blank=True, max_length=100)),
                ('brake_rear', models.CharField(blank=True, max_length=100)),
                ('suspension_front', models.CharField(blank=True, max_length=255)),
                ('suspension_rear', models.CharField(blank=True, max_length=255)),
                ('body_type', models.CharField(blank=True, max_length=100)),
                ('ABS', models.CharField(blank=True, max_length=100)),
                ('console', models.CharField(blank=True, max_length=100)),
                ('bike', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bikes_app.bikes')),
            ],
        ),
    ]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legion.settings')

import django
django.setup()

from bikes_app.models import BikeManufacturers, Bikes, BikeDetails

import csv
with open("Bike info - Sheet1.csv", 'r') as file:
    reader = csv.reader(file)
    column_names = next(reader)
    data_dict = dict()
    row_count = 0
    for row in reader:
        row_data = dict()
        for i in range(len(column_names)):
            row_data[column_names[i]] = row[i]

        data_dict[row_count] = row_data
        row_count += 1


    for key in data_dict:
        data = data_dict[key]

        manufacturer, created = BikeManufacturers.objects.get_or_create(name = data['Manufacturer'])

        if created == True:
            manufacturer.save()

        bike = Bikes()
        bike.model = data['model']
        bike.manufacturer = manufacturer
        bike.ex_showroom_price = data['ex_showroom_price']
        bike.image_link = data['image_link']
        bike.engine_displacement = data['engine_displacement']
        bike.variant = data['variant']

        bike.save()

        details = BikeDetails()
        details.bike = bike
        details.engine_type = data['engine_type']
        details.cooling_system = data['cooling_system']
        details.power = data['power']
        details.torque = data['torque']
        details.fuel_type = data['fuel_type']
        details.wheels = data['wheels']
        details.transmission = data['transmission']
        details.no_of_gears = data['no_of_gears']
        details.brake_front = data['brake_front']
        details.brake_rear = data['brake_rear']
        details.suspension_front = data['suspension_front']
        details.suspension_rear = data['suspension_rear']
        details.body_type = data['body_type']
        details.ABS = data['ABS']
        details.console = data['console']

        details.save()

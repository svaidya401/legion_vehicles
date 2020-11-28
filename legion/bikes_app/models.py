from django.db import models

# Create your models here.
class BikeManufacturers(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name

class Bikes(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(blank=True, max_length=255)
    manufacturer = models.ForeignKey(BikeManufacturers, on_delete=models.CASCADE)
    ex_showroom_price = models.CharField(blank=True, max_length=100)
    image_link = models.TextField(blank=True)
    engine_displacement = models.CharField(blank=True, max_length=100)
    variant = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return "{} {} {}".format(self.manufacturer, self.model, self.variant)

class BikeDetails(models.Model):
    bike = models.OneToOneField(Bikes, on_delete=models.CASCADE)
    engine_type = models.CharField(blank=True, max_length=255)
    cooling_system = models.CharField(blank=True, max_length=100)
    power = models.CharField(blank=True, max_length=100)
    torque = models.CharField(blank=True, max_length=100)
    fuel_type = models.CharField(blank=True, max_length=50)
    wheels = models.CharField(blank=True, max_length=100)
    transmission = models.CharField(blank=True, max_length=100)
    no_of_gears = models.CharField(blank=True, max_length=100)
    brake_front = models.CharField(blank=True, max_length=100)
    brake_rear = models.CharField(blank=True, max_length=100)
    suspension_front = models.CharField(blank=True, max_length=255)
    suspension_rear = models.CharField(blank=True, max_length=255)
    body_type = models.CharField(blank=True, max_length=100)
    ABS = models.CharField(blank=True, max_length=100)
    console = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return "{} {} {}".format(self.bike.manufacturer, self.bike.model, self.bike.variant)

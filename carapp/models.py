import datetime
from django.db import models
from django.contrib.auth.models import User
# pip install django-multiselectfield
from multiselectfield import MultiSelectField



# Create your models here.
class CarType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=10, decimal_places=4)
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)
    vehicle_description = models.CharField(blank=True, max_length=200)
    FEATURES_CHOICES = (
        ('CRUISE_CONTROL', 'Cruise Control'),
        ('AUDIO_INTERFACE', 'Audio Interface'),
        ('AIRBAGS', 'Airbags'),
        ('AIR_CONDITIONING', 'Air Conditioning'),
        ('SEAT_HEATING', 'Seat Heating'),
        ('PARK_ASSIST', 'ParkAssist'),
        ('POWER_STEERING', 'Power Steering'),
        ('REVERSING_CAMERA', 'Reversing Camera'),
        ('AUTO_START_STOP', 'Auto Start/Stop'),
    )
    features = MultiSelectField(choices=FEATURES_CHOICES, max_length=50, blank=True)

    def __str__(self):
        return self.car_name


class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
        ('CH', 'Chatham')]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='CH')
    interested_in = models.ManyToManyField(CarType)
    phone_number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Buyer'


class OrderVehicle(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    number_of_vehicles_ordered = models.PositiveIntegerField(default=0)
    order_status_choices = (
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    )
    order_status = models.IntegerField(choices=order_status_choices, default=1)
    order_updated_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.buyer.username

    def buyer_username(self):
        return self.buyer.username

    def total_price(self):
        return self.vehicle.car_price * self.number_of_vehicles_ordered


class Description(models.Model):
    title = models.CharField(max_length=20)
    project_description = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LabGroupMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    semester = models.IntegerField()
    personal_page = models.URLField()

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

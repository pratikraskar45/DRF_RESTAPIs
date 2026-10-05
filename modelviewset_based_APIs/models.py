from django.db import models


class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20, unique=True)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    VEHICLE_TYPES = [
        ('Truck', 'Truck'),
        ('Tempo', 'Tempo'),
        ('Bus', 'Bus'),
        ('Van', 'Van'),
        ('SUV', 'SUV'),
    ]

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPES
    )

    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    manufacturing_year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    registration_date = models.DateField()

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_number
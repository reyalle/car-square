from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    color = models.CharField(max_length=20)
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.color} {self.vin}"

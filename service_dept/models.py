from django.db import models
from sales_dept.models import Customer
from inventory.models import Car

class ServiceAppointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    details = models.TextField()


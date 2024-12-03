from django.db import models
from decimal import Decimal

class Component(models.Model):
    COMPONENT_TYPES = (
        ('new', 'New'),
        ('repair', 'Repair'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    component_type = models.CharField(max_length=10, choices=COMPONENT_TYPES)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

class Issue(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    description = models.TextField()
    is_repair_needed = models.BooleanField()

    def __str__(self):
        return f'{self.vehicle} - {self.component.name} issue'

class Transaction(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    transaction_date = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        total = Decimal('0.00')
        for issue in Issue.objects.filter(vehicle=self.vehicle):
            total += issue.component.price
        
        self.total_price = total
        self.save()

    def __str__(self):
        return f"Transaction ID: {self.id}, Total Price: {self.total_price:.2f}" 
    

class RevenueLog(models.Model):
    date = models.DateField(auto_now_add=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return f'Revenue on {self.date}'

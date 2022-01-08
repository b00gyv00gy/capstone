from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Trip(models.Model):
    name = models.CharField(max_length=128, default="empty")
    
    def __str__(self):
        return self.name

class Item(models.Model):
    trip = models.ForeignKey(Trip)
    name = models.CharField(max_length=128, default="empty")
    date = models.DateTimeField
    booked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    CHOICES = (
        ('EUR', 'euro'),
        ('USD', 'dollar'),
        ('RUB', 'ruble'),
    )
    item = models.ForeignKey(Item)
    amount = models.DecimalField
    currency = models.CharField(max_length=3, choices=CHOICES)
    who_paid = models.ForeignKey(User)

class Participant(models.Model):
    expense = models.ForeignKey(Expense)
    participant = models.ForeignKey(User)

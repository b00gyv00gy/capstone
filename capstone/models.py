from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    pass

class Trip(models.Model):
    name = models.CharField(max_length=128, default="empty")
    is_archived = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    CHOICES = (
        ('TRANSPORT', 'transport'),
        ('HOUSE', 'house'),
        ('SKI', 'ski'),
        ('FOOD', 'food'),
        ('', 'other')
    )

    trip = models.ForeignKey(Trip, on_delete=CASCADE)
    name = models.CharField(max_length=9, choices=CHOICES)
    link = models.URLField
    date = models.DateTimeField(auto_now_add=True, blank=True)
    booked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    CHOICES = (
        ('EUR', 'euro'),
        ('USD', 'dollar'),
        ('RUB', 'ruble'),
    )
    item = models.ForeignKey(Item, on_delete=CASCADE)
    amount = models.DecimalField
    currency = models.CharField(max_length=6, choices=CHOICES)
    who_paid = models.ForeignKey(User, on_delete=CASCADE)

class Participant(models.Model):
    expense = models.ForeignKey(Expense, on_delete=CASCADE)
    participant = models.ForeignKey(User, on_delete=CASCADE)

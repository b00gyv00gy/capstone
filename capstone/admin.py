from django.contrib import admin
from . models import User, Trip, Item, Expense, Participant

# Register your models here.
admin.site.register(User)
admin.site.register(Trip)
admin.site.register(Item)
admin.site.register(Expense)
admin.site.register(Participant)

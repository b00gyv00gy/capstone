import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.utils import Error
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Trip, Item, Expense, Participant


def index(request):

    if request.user.is_authenticated:
        current_trip = Trip.objects.filter(is_archived = False).first()
        archived_trips = Trip.objects.filter(is_archived = True)
        current_items = Item.objects.filter(trip=current_trip)
        expenses = Expense.objects.all()
        current_expenses = Expense.objects.none()
        for expense in expenses:
            current_expenses |= current_items.filter(pk=expense.item)
                

        return render(request, "capstone/index.html",{
        "current_trip": current_trip,
        "archived_trips": archived_trips,
        "current_items": current_items,
        "current_expenses": current_expenses,
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "capstone/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")

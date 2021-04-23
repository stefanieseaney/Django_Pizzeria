"""Defines URL patterns for pizzas"""
from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # List of Pizzas Page
    path("pizzas/", views.pizzas, name="pizzas"),
    # Pizza Topping Detail Page
    path("pizzas/<int:pizza_id>", views.pizza, name="pizza"),
]

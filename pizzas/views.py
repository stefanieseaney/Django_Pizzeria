from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.


def index(request):
    """Homepage."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Pizza list page."""
    pizzas = Pizza.objects.order_by("name")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    """Individual pizza page."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by("name")

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)
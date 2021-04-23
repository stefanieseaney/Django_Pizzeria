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

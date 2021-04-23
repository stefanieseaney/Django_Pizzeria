from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.


def index(request):
    """Homepage."""
    return render(request, "pizzas/index.html")

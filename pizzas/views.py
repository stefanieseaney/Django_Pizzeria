from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CommentForm

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
    comments = pizza.comment_set.order_by("-date_added")

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect("pizzas:pizza", pizza_id=pizza_id)

    context = {"pizza": pizza, "toppings": toppings, "comments": comments, "form": form}
    return render(request, "pizzas/pizza.html", context)
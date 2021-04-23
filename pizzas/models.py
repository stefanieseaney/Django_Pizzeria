from django.db import models

"""
1) Define a model Pizza with a field called name, which will hold name values,
   such as Hawaiian and Meat Lovers.
2) Define a model called Topping with fields called pizza and name.
   The pizza field should be a foreign key to Pizza, and name 
   should be able to hold values such as pineapple, Canadian bacon, and sausage.
3) Register both models with the admin site, and use the site to enter 
   some pizza names and toppings.
4) Pizzeria Home Page: Add a creative home page to your project to 
   replace the Django default home page
5) Add a page to the project that shows the names of available pizzas.
6) Link each pizza name to a page displaying the pizza and
   its pizza’s toppings. Add a picture for each pizza.
7) Create a form that allows users to post comments on 
   any particular pizza page
"""


class Pizza(models.Model):
    """Pizza creation."""

    name = models.CharField(max_length=256)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """Topping on pizza"""

    name = models.CharField(max_length=256)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Comment on a pizza"""

    comment = models.CharField(max_length=1024)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
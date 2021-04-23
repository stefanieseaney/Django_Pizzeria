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

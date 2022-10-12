from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.name

class Reviews(models.Model):
    # book = models.CharField(max_length=100)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    # user = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    rating = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Cart(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    options = (
        ("in-cart", "in-cart"),
        ("Cancelled", "Cancelled"),
        ("Order-Placed", "Order-Placed")
    )
    status = models.CharField(max_length=100, choices=options, default="in-cart")

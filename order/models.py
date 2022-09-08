import imp
from operator import mod
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from customer.models import Customer
from product.models import Product

class Order(models.Model):

    name = models.CharField(max_length = 255)
    description = models.TextField(null = True)
    customer_id = models.ForeignKey(Customer, related_name = "customer_id", on_delete = models.CASCADE)
    status = models.CharField(max_length=50, default = 'placed')

    created_at = models.DateField(auto_now_add = True)
    updated_at  = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'orders'


class OrderDetail(models.Model):

    order_id = models.ForeignKey(Order, related_name = 'order_id', on_delete = models.CASCADE, null = True)
    product_id = models.ForeignKey(Product, related_name = "product_id", on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length=50)

    created_at = models.DateField(auto_now_add = True)
    updated_at  = models.DateField(auto_now = True)

    def __str__(self):
        return self.product_id.name
    
    class Meta:
        db_table = 'order details'

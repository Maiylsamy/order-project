from django.db import models
from inventory.models import *
# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200,null=True)
    customer_since = models.DateField()
    
    def __str__(self):
        return self.customer_name
    
class Order(models.Model):
    Customer_reference = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product_reference = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order_number = models.IntegerField(default=0)
    order_date = models.DateField()
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    bill = models.FloatField(default=0)
    
    def __str__(self):
        return self.order_number


    
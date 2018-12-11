from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerId = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=10)
    CustomerAddr = models.CharField(max_length=50)
    CustomerCity = models.CharField(max_length=10)
class OrderTable(models.Model):
    OrderId = models.IntegerField(primary_key=True)
    OrderDate = models.DateTimeField(auto_now_add=True)
    CustomerId = models.ForeignKey('Customer')

class Product(models.Model):
    ProductId = models.IntegerField(primary_key=True)
    UnitPrice = models.DecimalField(max_digits=5,decimal_places=2)
    ProductName = models.CharField(max_length=20)
class OrderDetail(models.Model):
    # orderId = models.IntegerField(primary_key=True)
    # productId = models.IntegerField(primary_key=True)
    OrderId = models.ForeignKey('OrderTable')
    ProductId = models.ForeignKey('Product')
    Discount = models.DecimalField(max_digits=2,decimal_places=1)
    Quantity = models.IntegerField()

    class Mate:
        #设置两个字段组合在一起是唯一的
        unique_together = ("OrderId", "ProductId")




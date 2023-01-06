from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    available_quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField() # different from quantity because price will have decimal because of the cents.
    order_quantity = models.IntegerField(null=True)


    # def __str__(self):
    #     return self.name
      

# addressee indicates the recipient of the order not necessarily the person placing the order.
class Addressee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    # What is this here for?  
    # def __str__(self): 
    #     return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),)
    
    cart_items = models.ManyToManyField(Product, through="ProductsInOrder")
    addressee = models.ForeignKey(Addressee,on_delete=models.SET_NULL,null=True)
    total_price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    is_confirmed = models.BooleanField(default=False)



class ProductsInOrder(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity = models.IntegerField()

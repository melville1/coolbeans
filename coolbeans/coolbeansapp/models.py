from django.db import models

# Create your models here.
class Tag(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
            return self.type
    
    
      

# addressee indicates the recipient of the order not necessarily the person placing the order.
class Addressee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()

    
    def __str__(self):
            return self.name


class Product(models.Model):
    types = models.ManyToManyField(Tag)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True)
    price = models.FloatField() 
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),)
    addressee = models.ForeignKey(Addressee,on_delete=models.SET_NULL,null=True)
   
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='pending')
    
    def get_order_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 




class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0, null=True, blank=True)
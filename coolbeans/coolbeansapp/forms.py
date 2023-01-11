from django.forms import ModelForm
from coolbeansapp.models import ProductsInOrder, Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'






class ProductsInOrderForm(OrderForm):
    class Meta:
        model = ProductsInOrder
        fields = '__all__'


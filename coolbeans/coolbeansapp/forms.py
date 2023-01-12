from django.forms import ModelForm
from coolbeansapp.models import  Order,OrderItem





class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


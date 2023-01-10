from django.forms import ModelForm 
from coolbeansapp.models import ProductsInOrder

class ProductsInOrderForm(ModelForm):
    class Meta:
        model = ProductsInOrder
        fields = {'quantity'}


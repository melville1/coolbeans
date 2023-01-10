from django.shortcuts import render
from django.http import Http404
from django.views import View
from coolbeansapp.models import Product,Order, Addressee, ProductsInOrder
from coolbeansapp.forms import ProductsInOrderForm
# Create your views here.

class HomeView(View):
    def get (self,request):

        


        
        return render(
        request= request,
        template_name= "home.html",
        context= {}
        )
    

class OrderView(View):
    def get (self,request,):

        ProductsForm = ProductsInOrderForm()
        

      

        

        products = Product.objects.all()
        total = 0
        for product in products:
            total += product.price
        total = round(total,2)
        # # print(total)
        # get_quantity_and_product
        
        # for product in products:
        #     product = product * product.price

            
            



        html_data ={ 
            'products': products,
            'total': total,
            'ProductsForm': ProductsForm,
            
        }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )
    # def post(self,request):
    #     product_form = ProductsInOrderForm(request.POST)
    #     product_form.save()

    #     redirect('confirmation')

class ConfirmationView(View):
    def get (self,request,):
        # order = Order.objects.get(id=)

        
        
        return render(
        request= request,
        template_name= "confirmation.html",
        context= {}
        )

class ReceiptView(View):
    def get(self, request):
        pass

class ProductView(View):
    def get (self,request):
        
        
        return render(
        request= request,
        template_name= "product_list.html",
        context= {}
        )
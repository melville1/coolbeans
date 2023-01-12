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
    def get (self,request,id):

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
    def get (self,request,id):
        # order = Order.objects.get(id=)

        
        
        return render(
            request= request,
            template_name= "confirmation.html",
            context= {}
        )

class ReceiptView(View):
    def get(self, request, receipt):
        # I need to pull the most recent order number and products in order
        viewed_order = Order.objects.get(id=receipt)
        viewed_products = ProductsInOrder.objects.filter(order=receipt)
        all_products = Product.objects.all()
        total_price = viewed_order.get_total() 
        
        html_data = { 
            'viewed_order' : viewed_order,
            'viewed_products' : viewed_products,
            'total_price' : total_price,
        }

        return render(
            request =  request,
            template_name='receipt.html',
            context=html_data
        )



            


        

class ProductView(View):
    def get (self,request):
        # getting all objects from talbe Product
        products = Product.objects.all()
        # exportiing that data to a dictionary so the django template can interpret it
        html_data = {
            "product_list": products
        }
        return render(
            request= request,
            template_name= "product_list.html",
            context= html_data
        )
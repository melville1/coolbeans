from django.shortcuts import render, redirect
from django.views import View
from coolbeansapp.models import Product,Order, Addressee, ProductsInOrder
from coolbeansapp.forms import ProductsInOrderForm
from django.forms import formset_factory
from. forms import ProductsInOrderForm

# Create your views here.
class HomeView(View):
    def get (self,request):

        


        
        return render(
        request= request,
        template_name= "home.html",
        context= {}
        )

class OrderView(View):
    product_count = Product.objects.all().count()
    product_form_set = formset_factory(ProductsInOrderForm, extra=product_count)

    def get (self,request,):

        product_form_set = formset_factory(ProductsInOrderForm, extra=OrderView.product_count)
        
        
        products = Product.objects.all()
       
        formset = product_form_set()
        print(formset)

        # testform = ProductsInOrderForm
        
         # total = 0
        # for product in products:
        #     total += product.price
        # total = round(total,2)
        # # print(total)
        # get_quantity_and_product
        
        # for product in products:
        #     product = product * product.price

        html_data ={ 
            
            
            'products': products,
            # 'testform': testform,
            
            
            # 'total': total,
            'formset': formset
            
        }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )
    def post(self,request):
        product_form_set = formset_factory(ProductsInOrderForm, extra=OrderView.product_count-1)
        print(request.POST)
        formset = product_form_set(request.POST, request.FILES)   
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    products = form.save(commit=False)
                    products.save()
                    

        
        redirect('confirmation')


class ConfirmationView(View):
    def get (self,request):
        # order = Order.objects.get(id=)

            
        
        return render(
        request= request,
        template_name= "confirmation.html",
        context= {}
        )



class ReceiptView(View):
    def get (self,request):
        
        
        return render(
        request= request,
        template_name= "receipt.html",
        context= {}
        )



class ProductView(View):
       def get (self,request):
        
        
        return render(
        request= request,
        template_name= "product_list.html",
        context= {}
        )
from django.shortcuts import render, redirect
from django.views import View
from coolbeansapp.models import Product, Order, Addressee, OrderItem
from .forms import OrderItemForm
from django.forms import inlineformset_factory


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
                                    # The orders will be associated with table Addressee
                                    # second arguments specifies which table it will use to make forms
        OrderItemFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
    
        formset = OrderItemFormset()

       
        html_data ={ 
            'formset':formset
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )


    def post(self,request,id):
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
        addressee = Addressee.objects.get(id=id) # retrieveing a specific addressee
        order = Order.objects.create(addressee=addressee)
        formset = OrderFormset(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
        return redirect('confirmation', order.id )



class EditView(View):

    def get (self,request,id):
        order = Order.objects.get(id=id)
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'],)
        formset = OrderFormset(instance=order)

        html_data ={ 
            'formset':formset
            }


        return render(
            request= request,
            template_name= "order.html",
            context= html_data
        )

       
    def post(self,request,id):
        order= Order.objects.get(id=id)
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'],)
        formset = OrderFormset(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
        return redirect('confirmation', order.id )
        

        


   


class ConfirmationView(View):
    def get (self,request,id):
        order = Order.objects.get(id=id)
        orderitems = order.orderitem_set.all() # give me all the order associated with this customer
        

        return render(
            request=request,
            template_name='confirmation.html',
            context={
                'order':order,
                'items':orderitems,
            }
        )
    def post(self,request,id):
        order = Order.objects.get(id=id)
        orderitems = order.orderitem_set.all()
        if 'delete' in request.POST:
            order.delete()
            return redirect('home')
            
            

       

            
class ReceiptView(View):
    def get(self, request, receipt):
        # I need to pull the most recent order number and products in order
        viewed_order = Order.objects.get(id=receipt)
        viewed_products = OrderItem.objects.filter(order=receipt)
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
        # getting all objects from Product Table
        products = Product.objects.all()
        # exporting that data to a dictionary so the django template can interpret it
        html_data = {
            "product_list": products
        }
        return render(
            request= request,
            template_name= "product_list.html",
            context= html_data
        )
class AboutView(View):
    
    def get (self,request):
        return render(
            request= request,
            template_name= "about.html",
            context= {}
        )
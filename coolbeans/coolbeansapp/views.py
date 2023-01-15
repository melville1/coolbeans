from django.shortcuts import render, redirect
from django.views import View
from coolbeansapp.models import Product, Order, Addressee, OrderItem, Tag
from .forms import OrderItemForm, OrderForm
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
   
    

    def get (self,request):
                                    # The orders will be associated with the Order table
                                    # second arguments specifies which table it will use to make forms
                                    # we are then able to make one form from these 2 tables.
        OrderItemFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
        #inlineformfactory allow you to create multiple forms at once. makes it more efficient.
        # # the form will only contain attributes that are contain within orderitem table 
        formset = OrderItemFormset()
        form = OrderForm()
       
        html_data ={ 
            'formset':formset,
            'form': form
            }


        return render(
        request= request,
        template_name= "order.html",
        context= html_data
        )


    def post(self,request):
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'])
        Customer = request.POST["addressee"]
        addressee = Addressee.objects.get(id=Customer) # we are getting the addresse - a set up for the following line
        order = Order.objects.create(addressee=addressee) #order is created connecting it to the addressee
        formset = OrderFormset(request.POST, instance=order)
         # we are calling the OrderItemFormset and filling it with the post data and then associating with the 
        # order from line 54 the "instance" in this case means associating with the order
        # what is happening here is that line 50 calls the form because the post needs it, then 
        # we get the adresse id this is the set up for the follwing line (52)because we will then 
        # create an order and associate it with the addressee and his/her info
        #line 54 then passes the data that was created from the addresse which was created in the post and associates 
        # to the order from line 53
        if formset.is_valid():
            formset.save()
        return redirect('confirmation', order.id )
        # this redirects us to confirmation 
        # the second argument "create.id" grabs the id from the order it does this because an object was created
        # from line 53, therefore we not only access to the id but any other attribute that object may contain
        # keep in mind this order.id now contains data


class EditView(View):

    def get (self,request,id):
        order = Order.objects.get(id=id)
        OrderFormset = inlineformset_factory(Order,OrderItem, fields=['product','quantity'],)
        formset = OrderFormset(instance=order)
    # the order id is from the previous view here we are accessing and displaying that order 
    # which is why you see it prefilled.

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
        #line 95 -whatever new data was put in the post whether it remains the same or not gets resent to the form
        # associated with that orderid 

class ConfirmationView(View):
    def get (self,request,id): # the id is like a book but only contains the title
        order = Order.objects.get(id=id) # we write this again because we need to acceess the book ( in this case order)
        # the order.objects.get will get me the order associated with id
        # this gets the entire object and all the data that it contains
        orderitems = order.orderitem_set.all() # the "_set.all()" is a django method thats allows us
        # to get everything from orderitem in this example.
        item_total = Order.get_order_items(order) 
        order_price = round(Order.get_total(order),2)
        
        
        return render(
            request=request,
            template_name='confirmation.html',
            context={
                'order':order,
                'items':orderitems,
                'order_total': item_total,
                'order_price': order_price,    
            })
    
        
    def post(self,request,id):
        order = Order.objects.get(id=id)
        orderitems = order.orderitem_set.all()
        if 'delete' in request.POST:
            order.delete()
            return redirect('home')  

            
class ReceiptView(View):
    def get(self, request, id):
        # I need to pull the most recent order number and products in order
        viewed_order = Order.objects.get(id=id)
        viewed_products = OrderItem.objects.filter(order=viewed_order)
        total_price = viewed_order.get_total() 

        html_data = { 
            'order' : viewed_order,
            'items' : viewed_products,
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
        # tags = []
        # Tag.objects.filter()
        #ing that data to a dictionary so the django template can interpret it
        for product in products:
            print(product.types.all())

        html_data = {
            "product_list": products,
            
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
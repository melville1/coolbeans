from django.shortcuts import render
from django.http import Http404
from django.views import View
# Create your views here.

class HomeView(View):
    def get (self,request):

        


        
        return render(
        request= request,
        template_name= "home.html",
        context= {}
        )
    

class OrderView(View):
    def get(self, request):
        pass

class ConfirmationView(View):
    def get(self, request):
        pass

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
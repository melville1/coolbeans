from django.urls import path

from coolbeansapp.views import HomeView, OrderView, ConfirmationView, ReceiptView, ProductView, EditView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order' , OrderView.as_view(), name='order' ),
    path('confirmation/<int:id>', ConfirmationView.as_view(), name='confirmation' ),
    path('editorder/<int:id>', EditView.as_view(), name='editorder' ),
    path('order/<int:id>', ReceiptView.as_view(), name='receipt' ),
    path('products/', ProductView.as_view(), name = 'product_list'),
    path('about/', AboutView.as_view(), name ='about')
   ]


from django.urls import path
from coolbeansapp.views import HomeView, OrderView, ConfirmationView, ReceiptView, ProductView, AboutView   

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order' , OrderView.as_view(), name='order'),
    path('confirmation', ConfirmationView.as_view(), name='confirmation'),
    path('order/<int>', ReceiptView.as_view(), name='receipt' ),
    path('products/', ProductView.as_view(), name = 'product_list'),
    path('about/', AboutView.as_view(), name ="about")
    ]

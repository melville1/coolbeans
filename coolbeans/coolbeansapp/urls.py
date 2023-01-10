from django.urls import path
from coolbeansapp.views import HomeView, OrderView, ConfirmationView, ReceiptView, ProductView, OrderHistoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order' , OrderView.as_view(), name='order'),
    path('confirmation', ConfirmationView.as_view(), name='confirmation'),
    path('order', ReceiptView.as_view(), name='receipt' ),
    path('products', ProductView.as_view(), name = 'product'),
    path('order_history', OrderHistoryView.as_view(), name = 'history'),

]

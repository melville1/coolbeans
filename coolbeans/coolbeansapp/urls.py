from django.urls import path
from coolbeansapp.views import HomeView, OrderView, ConfirmationView, ReceiptView, ProductView, EditView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('place_order/<int:id>' , OrderView.as_view(), name='order' ),
    path('confirmation/<int:id>', ConfirmationView.as_view(), name='confirmation' ),
    path('editorder/<int:id>', EditView.as_view(), name='editorder' ),
    path('receipt', ReceiptView.as_view(), name='receipt' ),
    path('products', ProductView.as_view(), name = 'product'),
]

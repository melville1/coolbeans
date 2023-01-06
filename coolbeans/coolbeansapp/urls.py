from django.urls import path
from coolbeansapp.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

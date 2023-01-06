from django.shortcuts import render
from django.http import Http404
from django.views import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        pass
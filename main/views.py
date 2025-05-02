from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, template_name='index.html')
def shop(request):
    return render(request, template_name='shop.html')
def cart(request):
    return render(request, template_name='cart.html')



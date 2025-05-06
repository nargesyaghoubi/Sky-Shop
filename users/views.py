from django.shortcuts import render


def signup(request):
     return render(request, template_name='signup.html')

def signin(request):
     return render(request, template_name='signin.html')
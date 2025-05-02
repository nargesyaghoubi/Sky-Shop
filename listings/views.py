from django.shortcuts import render

def listings(request):
    return render(request, template_name='listings.html')

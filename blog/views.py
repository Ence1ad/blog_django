from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, template_name='blog/index.html')

def get_category(request, slug):
    return render(request, template_name='blog/category.html')
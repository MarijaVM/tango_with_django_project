from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage':'What a day, what a day!',
                    'categories':category_list}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'message':'Rango says the about page'}
    return render(request, 'rango/about.html', context=context_dict)
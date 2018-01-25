from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage':'What a day, what a day!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'message':'Rango says the about page'}
    return render(request, 'rango/about.html', context=context_dict)
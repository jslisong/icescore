from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello')


def hello(request, name):
    context = {'name': name}
    return render(request, 'hello/index.html', context)


def home(request):
    return render(request, 'home.html')

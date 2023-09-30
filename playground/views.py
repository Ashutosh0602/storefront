from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action


def calculate():
    x = 231
    y = 26
    return x+y


def say_hello(request):
    calc = calculate()
    return render(request, 'hello.html', {"name": calc})

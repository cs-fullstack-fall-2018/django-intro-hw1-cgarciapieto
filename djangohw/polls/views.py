from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. ")


def user(request, user):

    if user == 'blue':
        print("SKY")
    elif user == 'red':
        print("FIRE")
    else:
        print("ERROR")

    return HttpResponse(user)
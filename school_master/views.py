from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,'school_master/index.html')


def login(request):
    return render(request,'school_master/login.html')
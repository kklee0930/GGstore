from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def detail(request):
    return render(request, "detail.html")

def shop(request):
    return render(request, "shop.html")

def cost(request):
    return render(request, "cost.html")
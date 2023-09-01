from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base.html")

def product(request):
    return render(request, "product.html")

def uploadRoute(request):
    if request.method == "POST" and request.FILES['file']:
        NONE
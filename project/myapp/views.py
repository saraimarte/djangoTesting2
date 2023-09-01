from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "base.html")

def product(request):
    return render(request, "product.html")

def upload(request):
    if request.method == "POST" and request.FILES['file'] and request.FILES['file2']:
        file1 = request.FILES['file']
        file2 = request.FILES['file2']
        return HttpResponse("Files Received.")
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def Services(request):
    return render(request,'Services.html')
def Gallery(request):
    return render(request,'Gallery.html')
def Contact(request):
    return render(request, 'Contact.html')

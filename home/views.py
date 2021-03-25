from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")
    #return HttpResponse("This is my website")

def sign(request):
    return render(request, "sign.html")
    #return HttpResponse("This is sign up page")

def login(request):
    return render(request, "login.html")
    #return Httpresponse("this is login page")
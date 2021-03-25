from django.shortcuts import render,HttpResponse
from home.models import Contact

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

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        contact = Contact(firstname = firstname, lastname = lastname, email = email, subject = subject)
        contact.save()
    return render(request, "contact.html")
    #return Httpresponse("this is contact page")
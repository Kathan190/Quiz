from django.shortcuts import render,HttpResponse
from home.models import Contact
from home.models import Sign
from home.models import Login

# Create your views here.

def home(request):
    return render(request, "home.html")
    #return HttpResponse("This is my website")

def sign(request):
    if request.method == "POST":
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        psw_repeat = request.POST.get("psw-repeat")
        sign = Sign(email = email, psw = psw, psw_repeat = psw_repeat)
        sign.save()
    return render(request, "sign.html")
    #return HttpResponse("This is sign up page")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        login = Login(email = email, psw = psw)
        login.save()
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
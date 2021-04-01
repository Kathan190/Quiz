from django.shortcuts import render,HttpResponse
from home.models import Signup
from home.models import Contact
from home.models import Login
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        #signup database code
        if request.POST.get("Signup") == "Signup":
            email = request.POST.get('email')
            psw = request.POST.get('psw')
            psw_repeat = request.POST.get('psw_repeat')
            print(email,psw,psw_repeat)

            if len(email)<5 or len(psw)<5 or (psw_repeat == psw):
                messages.error(request, 'Please fill the form correctly')
            else:
                signup = Signup(email=email,psw=psw,psw_repeat=psw_repeat)
                signup.save()
                messages.success(request, "Your account is successfully created")

        
        #contact database code
            if request.POST.get("Contact") == "Contact":
                email = request.POST.get('email1')
                contact = request.POST.get('contact')
                subject = request.POST.get('subject')
                con = Contact(email=email,contact=contact,subject=subject)
                con.save()
    
        #login database code
        if request.POST.get("Login") == "Login":
            email = request.POST.get('email')
            psw = request.POST.get('psw')
            login = Login(email=email,psw=psw)
            login.save()
    
    return render(request, "home.html")
    #return HttpResponse("This is my website")


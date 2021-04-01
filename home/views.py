from django.shortcuts import render,HttpResponse
from home.models import Signup

# Create your views here.

def home(request):
    if request.method == "POST":
        if request.POST.get("Signup") == "Signup":
            email = request.POST.get('email')
            psw = request.POST.get('psw')
            psw_repeat = request.POST.get('psw_repeat')
            if psw == psw_repeat:
                signup = Signup(email=email, psw=psw, psw_repeat=psw_repeat)
                signup.save()  
            else:
                return HttpResponse("Password is incorrect")
    return render(request, "home.html")
    #return HttpResponse("This is my website")


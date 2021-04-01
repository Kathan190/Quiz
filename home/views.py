from django.shortcuts import render,HttpResponse
from home.models import Signup

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        psw_repeat = request.POST.get('psw_repeat')
        signup = Signup(email=email, psw=psw, psw_repeat=psw_repeat)
        signup.save()        
    return render(request, "home.html")
    #return HttpResponse("This is my website")


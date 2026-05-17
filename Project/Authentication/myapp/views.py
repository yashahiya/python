from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def home(request):
    return render(request,"home.html")

def index(request):
    if request.method=="POST":
        em=request.POST["email"]
        pa=request.POST["password"]

        user=usersignup.objects.filter(email=em,password=pa)
        name=usersignup.objects.get(email=em)
        print(name.fullname)
        if user:
            print("login successfully")
            return redirect('login')
        else:
            print("Errors!")
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully")
        else:
            print(form.errors)
    return render(request,"signup.html")
def login(request):
    return render(request,"login.html")
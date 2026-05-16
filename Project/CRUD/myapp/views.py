from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=="POST":
        form=studform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted....")
        else:
            print(form.errors)

    return render(request,'index.html')

def show(request):
    stdata=studinfo.objects.all()
    return render(request,"show.html",{'stdata':stdata})

def update(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=="POST":
        form=studform(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record Inserted")
        else:
            print(form.errors)
    return render(request,"update.html",{"stid":stid})

def delete(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect("show")
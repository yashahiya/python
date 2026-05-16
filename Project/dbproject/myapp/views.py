from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=="POST":
        form=studform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted")
        else :
            print(form.errors)

    return render(request,"index.html")

def show_data(request):
    stdata=studinfo.objects.all()
    return render(request,"show_data.html",{'stdata':stdata})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect("showdata")

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=="POST":
        form=studform(request.POST,instance=stid)
        if form.is_valid():
            form.save()
            print("Record Inserted")
        else :
            print(form.errors)
    return render(request,"update_data.html",{"stid":stid})
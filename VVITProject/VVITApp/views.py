from django.shortcuts import render,redirect
from .forms import UsregForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'CSM-C/home.html')

def about(request):
    return render(request,'CSM-C/about.html')

def register(request):
    if request.method == "POST":
        p = UsregForm(request.POST)
        if p.is_valid():
           p.save()
           messages.success(request, "User registered Successfully")
           return redirect('/reg/')
    
    p = UsregForm()
    return render(request,'CSM-C/reg.html',{'z':p})
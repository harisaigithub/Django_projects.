from django.shortcuts import render,redirect
from .forms import StForm 
from .models import StReg
from django.contrib import messages

# Create your views here.
def stdnt(request):
    n = StReg.objects.all()
    if request.method == "POST":
        g = StForm(request.POST)
        if g.is_valid():
            g.save()
            messages.success(request, "Student Registered Successfully")
        return redirect('/st/')
    g = StForm()
    return render(request, 'Student/stdnt.html',{'v':g, 'h':n})

def stdup(request,z):
    q = StReg.objects.get(id=z)
    if request.method == "POST":
        p = StForm(request.POST,instance=q)
        if p.is_valid():
            p.save()
            messages.info(request, "Student Detailes updated Successfully")
            return redirect('/st/')
    p = StForm(instance=q)
    return render(request, 'Student/stdupd.html', {'d':p})

def stdtl(request,a):
    k = StReg.objects.get(id=a)
    if request.method == "POST":
        k.delete()
        messages.warning(request, "Student Deleted Successfully")
        return redirect('/st/')
    return render(request, 'Student/stdlte.html',{'c':k} )

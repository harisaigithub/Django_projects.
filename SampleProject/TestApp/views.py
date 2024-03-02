from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp 

# Create your views here.
def hek(k):
	return HttpResponse("Welcome User")

def gy(y):
	return HttpResponse("<h2>Welcome User</h2>")

def hk(request,n):
	return HttpResponse(f"Hi User {n}")

def byh(request,a,g):
	return HttpResponse(f"Hi user username: {g} Age: {a}")

def kn(request,cn,sn,rn):
	return HttpResponse(f"Name: <span style='color:green'>{cn}</span> Roll number: <span style='color:red'>{sn}</span> Age: <span style='color:blue'>{rn}</span>")

def km(request):
	return render(request,'demo.html')

def vh(request,k):
	return render(request,'sample.html',{"h":k})

def wh(request):
	if request.method == "POST":
		a = request.POST['sn']
		b = request.POST['sr']
		c = request.POST['sb']
		return render(request,'stdata.html',{'p':a,'q':b,'r':c})
	return render(request,'streg.html')

def emp(request):
	y = Emp.objects.all()
	if request.method == "POST":
		i = request.POST['a']
		j = request.POST['b']
		k = request.POST['c']
		l = request.POST['d']
		m = request.POST['e']
		g = Emp(eid=i,ename=j,eage=k,esal=l,edesg=m)
		g.save()
		return redirect('/')
	return render(request,'employee.html',{'p':y})

def emup(request,h):
	g = Emp.objects.get(id=h)
	if request.method == "POST":
		#b=Emp(eid=request.POST['ea'],ename=request.POST['eb'],eage=request.POST['ec'],esal=request.POST['ed'],edesg=request.POST['ee'])
		#b.save()
		g.eid=request.POST['ea']
		g.ename=request.POST['eb']
		g.eage=request.POST['ec']
		g.esal=request.POST['ed']
		g.edesg=request.POST['ee']
		g.save()
		return redirect('/')
	return render(request,'emupdate.html',{'e':g})
def emdt(request,w):
	z = Emp.objects.get(id=w) 
	if request.method == "POST":
		z.delete()
		return redirect('/')
	return render(request,'emdtld.html',{'d':z})
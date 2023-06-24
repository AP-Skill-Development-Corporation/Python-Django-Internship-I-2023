from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StForm
from django.core.mail import send_mail
from DemoProject import settings
from django.contrib import messages
# Create your views here.

def sa(request):
	return HttpResponse("Good Morning")

def printname(request,p):
	return HttpResponse(f"Good Morning {p}")

def stdtls(request,n,a):
	return HttpResponse(f"Student Details<br>Name: {n}<br>Age: {a}")

def empdtls(request,eage,epid,ename):
	return HttpResponse(f"<h3>Employee Data</h3><h4>Employee Name: {ename}</h4><h4>Employee Id: {epid}</h4><h4>Employee Age: {eage}</h4>")

def stprint(request,sid,stname):
	return HttpResponse(f"<h3>Student Name: <span style='background-color:green;color:white'>{stname}</span></h3><h3>Student Id: <i style='background-color:yellow;color:blue'>{sid}</i></h3>")

def eprint(request,ename):
	return HttpResponse("<style>span{background-color:cadetblue;color:white}</style><h4>Employee Name: <span>%s</span></h4>"%(ename))

def jprint(request,sname,y):
	return HttpResponse(f"<script>alert('Hi welcome User {sname}')</script><h4>Welcome User {sname}</h4><h5>Age: {y}</h5>")

def gy(request):
	return HttpResponse("<html><head><title>Demo Html Page</title></head><body>Hi User</body></html>")

def vb(request):
	return render(request,'demo.html')

def idt(request):
	return render(request,'html/index.html')

def dy(request):
	return render(request,'html/sample.html')

def btp(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	if request.method == "POST":
		e = request.POST['em'].split(',')
		s = request.POST['sb']
		d = request.POST['des']
		y = settings.EMAIL_HOST_USER
		z = send_mail(s,d,y,e)
		if z==1:
			messages.success(request,"Mail Sent Successfully")
			return redirect('/cnt')
		else:
			return HttpResponse("Not Sent")
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		r = request.POST['rn']
		n = request.POST['nm']
		e = request.POST['em']
		age = request.POST['ag']
		return render(request,'html/display.html',{'a':r,'b':n,'c':e,'d':age})
	return render(request,'html/register.html')

def index(request):
	w = Student.objects.all()
	if request.method == "POST":
		a = request.POST['r']
		b = request.POST['n']
		c = request.POST['y']
		d = request.POST['b']
		e = request.POST['a']
		z = Student(sroll=a,sname=b,syear=c,sbranch=d,sage=e)
		z.save()
		return redirect('/')
	return render(request,'html/dy.html',{'st':w})

def stupdate(request,w):
	f = Student.objects.get(id=w)
	if request.method == "POST":
		f.sname = request.POST['n']
		f.syear = request.POST['y']
		f.sbranch = request.POST['b']
		f.sage = request.POST['a']
		f.save()
		return redirect("/")
	return render(request,'html/stupd.html',{'s':f})

def stdel(request,y):
	p = Student.objects.get(id=y)
	if request.method == "POST":
		p.delete()
		return redirect('/')
	return render(request,'html/stdel.html',{'h':p})

def home(request):
	return render(request,'html/ind.html')

def abou(request):
	return render(request,'html/abt.html')

def stdetails(request):
	k = Student.objects.all()
	if request.method == "POST":
		c = StForm(request.POST)
		if c.is_valid():
			c.save()
			return redirect('/dt')
	c = StForm()
	return render(request,'html/liststd.html',{'w':c,'n':k})

def stp(request,s):
	h = Student.objects.get(id=s)
	if request.method == "POST":
		g = StForm(request.POST,instance=h)
		if g.is_valid():
			g.save()
			return redirect('/dt')
	g = StForm(instance=h)
	return render(request,'html/stpd.html',{'d':g,'p':h})

def sd(request,b):
	d = Student.objects.get(id=b)
	if request.method=="POST":
		d.delete()
		return redirect('/dt')
	return render(request,'html/stdl.html',{'a':d})
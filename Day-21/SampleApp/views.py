from django.shortcuts import render
from django.http import HttpResponse
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
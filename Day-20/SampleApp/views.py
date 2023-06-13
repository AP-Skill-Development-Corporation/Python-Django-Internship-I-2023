from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sa(request):
	return HttpResponse("Good Morning")

def printname(request,p):
	return HttpResponse(f"Good Morning {p}")

def stdtls(request,n,a):
	return HttpResponse(f"Student Details<br>Name: {n}<br>Age: {a}")
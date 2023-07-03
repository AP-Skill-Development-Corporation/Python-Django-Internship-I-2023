from django.shortcuts import render,redirect
from . forms import UsForm,TprofileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		s = UsForm(request.POST)
		if s.is_valid():
			h = s.save(commit=False)
			messages.success(request,f"{h.username} User Createdd Successfully")
			h.save()
			return redirect('/lgo')
	s = UsForm()
	return render(request,'html/register.html',{'p':s})

@login_required
def profile(request):
	return render(request,'html/profile.html')

@login_required
def updpf(request):
	if request.user.role_type == 2:
		tch = TprofileForm()
	return render(request,'html/updateprofile.html',{'t':tch})
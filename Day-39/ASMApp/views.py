from django.shortcuts import render,redirect
from . forms import UsForm,TprofileForm,SprofileForm
from . models import TeacherProfile,StudentProfile
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
		x = TeacherProfile.objects.all()
		mx = []
		for i in x:
			mx.append(i.tch_id)
		if request.user.id not in mx:
			if request.method == "POST":
				tch = TprofileForm(request.POST)
				if tch.is_valid():
					t = tch.save(commit=False)
					t.tstatus = 1
					t.tch_id = request.user.id
					t.save()
					messages.info(request,"Profile Created Successfully")
					return redirect('/pfe')
			tch = TprofileForm()
			return render(request,'html/updateprofile.html',{'t':tch})
		else:
			z = TeacherProfile.objects.get(tch_id=request.user.id)
			if request.method == "POST":
				c = TprofileForm(request.POST,instance=z)
				if c.is_valid():
					c.save()
					messages.warning(request,"Profile Updated Successfully")
					return redirect('/pfe')
			c = TprofileForm(instance=z)
			return render(request,'html/updateprofile.html',{'ty':c})
	elif request.user.role_type == 1:
		s = StudentProfile.objects.all()
		w = []
		for i in s:
			w.append(i.std_id)
		if request.user.id not in w:
			if request.method == "POST":
				v = SprofileForm(request.POST)
				if v.is_valid():
					q = v.save(commit=False)
					q.sstatus = 1
					q.std_id = request.user.id
					q.save()
					messages.success(request,"Profile Created Successfully")
					return redirect('/pfe')
			v = SprofileForm()
			return render(request,'html/updateprofile.html',{'g':v})
		else:
			ku = StudentProfile.objects.get(std_id=request.user.id)
			if request.method == "POST":
				bg = SprofileForm(request.POST,instance=ku)
				if bg.is_valid():
					bg.save()
					messages.info(request,'Profile Updated Successfully')
					return redirect('/pfe')	
			bg = SprofileForm(instance=ku)
			return render(request,'html/updateprofile.html',{'hn':bg})
	else:
		pass

@login_required
def tsgnlist(request):
	return render(request,'html/taslist.html')
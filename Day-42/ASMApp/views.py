from django.shortcuts import render,redirect
from . forms import UsForm,TprofileForm,SprofileForm,AstForm
from . models import TeacherProfile,StudentProfile,AssignmentT,AssignmentSt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
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
	b = AssignmentT.objects.filter(atch_id=request.user.id)
	if request.method == "POST":
		y= AstForm(request.POST)
		if y.is_valid():
			h = y.save(commit=False)
			h.astatus = 1
			h.atch_id = request.user.id
			h.save()
			return redirect('/tasgn')
	y = AstForm()
	return render(request,'html/taslist.html',{'e':y,'p':b})

@login_required
def astup(request,v):
	y = AssignmentT.objects.get(id=v)
	if request.method == "POST":
		d = AstForm(request.POST,instance=y)
		if d.is_valid():
			d.save()
			return redirect('/tasgn')
	d = AstForm(instance=y)
	return render(request,'html/astupdate.html',{'r':d})

@login_required
def adlt(request,g):
	n = AssignmentT.objects.get(id=g)
	if request.method == "POST":
		n.delete()
		return redirect('/tasgn')
	return render(request,'html/asdel.html',{'k':n})

@login_required
def staslist(request):
	p = AssignmentT.objects.filter(abranch=request.user.studentprofile.sbranch,ayear=request.user.studentprofile.syear)
	return render(request,'html/staslist.html',{'e':p})

@login_required
def astt(request,h):
	j = AssignmentT.objects.get(id=h)
	q = AssignmentSt.objects.filter(ssd_id=request.user.id)
	print(q)
	# if h not in t.values():
	# 	if request.method == "POST":
	# 		y = AssignmentSt(san=j.aname,ssubject=j.asubject,scrted=datetime.now().date(),sactive='1',asd_id=h,ssd_id=request.user.id)
	# 		y.save()
	# 		return redirect('/stlist')
	return render(request,'html/asact.html',{'c':j})
from django.shortcuts import render,redirect
from . forms import UsForm,TprofileForm,SprofileForm,AstForm,AsstForm,SsubForm,TsForm,AdrolU,UsplForm
from . models import TeacherProfile,StudentProfile,AssignmentT,AssignmentSt,User
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
	ut = User.objects.get(id=request.user.id)
	if request.user.role_type == 2:
		x = TeacherProfile.objects.all()
		mx = []
		for i in x:
			mx.append(i.tch_id)
		if request.user.id not in mx:
			if request.method == "POST":
				tch = TprofileForm(request.POST)
				pfe = UsplForm(request.POST,request.FILES,instance=ut)
				if tch.is_valid() and pfe.is_valid():
					t = tch.save(commit=False)
					t.tstatus = 1
					t.tch_id = request.user.id
					t.save()
					pfe.save()
					messages.info(request,"Profile Created Successfully")
					return redirect('/pfe')
			tch = TprofileForm()
			pfe = UsplForm(instance=ut)
			return render(request,'html/updateprofile.html',{'t':tch,'u':pfe})
		else:
			z = TeacherProfile.objects.get(tch_id=request.user.id)
			if request.method == "POST":
				c = TprofileForm(request.POST,instance=z)
				pfe = UsplForm(request.POST,request.FILES,instance=ut)
				if c.is_valid() and pfe.is_valid():
					c.save()
					pfe.save()
					messages.warning(request,"Profile Updated Successfully")
					return redirect('/pfe')
			c = TprofileForm(instance=z)
			pfe = UsplForm(instance=ut)
			return render(request,'html/updateprofile.html',{'ty':c,'u':pfe})
	elif request.user.role_type == 1:
		s = StudentProfile.objects.all()
		w = []
		for i in s:
			w.append(i.std_id)
		if request.user.id not in w:
			if request.method == "POST":
				v = SprofileForm(request.POST)
				pfe = UsplForm(request.POST,request.FILES,instance=ut)
				if v.is_valid() and pfe.is_valid():
					q = v.save(commit=False)
					q.sstatus = 1
					q.std_id = request.user.id
					q.save()
					pfe.save()
					messages.success(request,"Profile Created Successfully")
					return redirect('/pfe')
			v = SprofileForm()
			pfe = UsplForm(instance=ut)
			return render(request,'html/updateprofile.html',{'g':v,'u':pfe})
		else:
			ku = StudentProfile.objects.get(std_id=request.user.id)
			if request.method == "POST":
				bg = SprofileForm(request.POST,instance=ku)
				pfe = UsplForm(request.POST,request.FILES,instance=ut)
				if bg.is_valid():
					bg.save()
					pfe.save()
					messages.info(request,'Profile Updated Successfully')
					return redirect('/pfe')	
			bg = SprofileForm(instance=ku)
			pfe = UsplForm(instance=ut)
			return render(request,'html/updateprofile.html',{'hn':bg,'u':pfe})
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
	nk = AssignmentSt.objects.filter(ssd_id=request.user.id)
	df,sf = {},{}
	for i in nk:
		df[i.asd_id] = i.asd_id,i.id,i.sactive
	for j in p:
		if j.id in df:
			if df[j.id][2] == "1":
				sf[j.id] = j.id,j.aname,j.asubject,j.astartdate,j.aenddate,j.amarks,j.astatus,j.atch_id,'1'
			elif df[j.id][2] == "2":
				sf[j.id] = j.id,j.aname,j.asubject,j.astartdate,j.aenddate,j.amarks,j.astatus,j.atch_id,'2'
			else:
				sf[j.id] = j.id,j.aname,j.asubject,j.astartdate,j.aenddate,j.amarks,j.astatus,j.atch_id,'3'
		else:
			sf[j.id] = j.id,j.aname,j.asubject,j.astartdate,j.aenddate,j.amarks,j.astatus,j.atch_id,'0'
	print(sf.values())
	return render(request,'html/staslist.html',{'e':sf.values()})

@login_required
def astt(request,h):
	j = AssignmentT.objects.get(id=h)
	q = AssignmentSt.objects.filter(asd_id=h,ssd_id=request.user.id)
	t = []
	for i in q:
		t.append(i.asd_id)
	if h not in t:
		if request.method == "POST":
			y = AssignmentSt(san=j.aname,ssubject=j.asubject,scrted=datetime.now().date(),sactive='1',asd_id=h,ssd_id=request.user.id)
			y.save()
			return redirect('/stlist')
		return render(request,'html/asact.html',{'c':j})
	else:
		return render(request,'html/asact.html',{'w':t})

@login_required
def stsblst(request):
	z = AssignmentSt.objects.filter(ssd_id=request.user.id)
	return render(request,'html/stsblst.html',{'p':z})

@login_required
def ssbup(request,t):
	s = AssignmentSt.objects.get(id=t)
	if request.method == "POST":
		m = AsstForm(request.POST,instance=s)
		if m.is_valid():
			m.save()
			return redirect('/ssblst')
	m = AsstForm(instance=s)
	return render(request,'html/sstup.html',{"k":m})

@login_required
def ssubf(request,m):
	h = AssignmentSt.objects.get(id=m)
	if request.method == "POST":
		v = SsubForm(request.POST,instance=h)
		if v.is_valid():
			z=v.save(commit=False)
			z.sactive='3'
			z.ssubd = datetime.now().date()
			z.save()
			return redirect('/ssblst')
	v = SsubForm(instance=h)
	return render(request,'html/ssubf.html',{'pp':v})

@login_required
def tstup(request):
	y = AssignmentT.objects.filter(atch_id=request.user.id)
	u = User.objects.all()
	p = AssignmentSt.objects.all()
	s,fnl,g,mk = {},{},[],{}
	for t in u:
		s[t.id] = t.id,t.eid
	for i in y:
		g.append(i.id)
	for j in p:
		if j.asd_id in g:
			mk[j.id] = j.id,j.san,j.ssubject,j.ssd_id,j.sactive
	for k in mk.items():
		if k[1][3] in s:
			if k[1][4] == '3':
				fnl[[k][0]]=k[0],k[1][1],k[1][2],s[k[1][3]][1]
	return render(request,'html/tstup.html',{'fg':fnl.values})

@login_required
def tsmrup(request,p):
	m = AssignmentSt.objects.get(id=p)
	if request.method == "POST":
		k = TsForm(request.POST,instance=m)
		if k.is_valid():
			k.save()
			return redirect('/tst')
	k = TsForm(instance=m)
	return render(request,'html/tsmrk.html',{'m':k})

@login_required
def adlistv(request):
	g = User.objects.filter(is_superuser=0)
	if request.method == "POST":
		m = UsForm(request.POST)
		if m.is_valid():
			m.save()
			return redirect('/adlist')
	m = UsForm()
	return render(request,'html/adlist.html',{'k':m,'p':g})

@login_required
def adups(request,j):
	p = User.objects.get(id=j)
	if request.method == "POST":
		n = AdrolU(request.POST,instance=p)
		print(n)
		if n.is_valid():
			n.save()
			return redirect('/adlist')
	n = AdrolU(instance=p)
	return render(request,'html/adsupd.html',{'nk':n})
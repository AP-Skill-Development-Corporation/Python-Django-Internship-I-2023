from django import forms
from . models import User,TeacherProfile,StudentProfile,AssignmentT,AssignmentSt
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class UsForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","eid"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Unique Id",
			}),
		}

class TprofileForm(forms.ModelForm):
	class Meta:
		model = TeacherProfile
		fields = ["tage","tgr",'tbranch','tsubject','texpr','tdesg']
		widgets = {
		"tage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your age",
			}),
		"tgr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"tbranch":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Branch",
			}),
		"tsubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Subject",
			}),
		"texpr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Experience",
			}),
		"tdesg":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Designation",
			}),
		}

class SprofileForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ["stage","sgr","sbranch","syear"]
		widgets = {
		"stage":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your age",
			}),
		"sgr":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"sbranch":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"syear":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class AstForm(forms.ModelForm):
	class Meta:
		model = AssignmentT
		fields = ["anm","aname","ayear","abranch","asubject","astartdate","aenddate","amarks","adesc","astatus"]
		widgets = {
		"anm":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn number",
			}),
		"aname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn Name",
			}),
		"ayear":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"abranch":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"asubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Subject Name",
			}),
		"astartdate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"aenddate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		"amarks":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		"adesc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Assgn Desc",
			"rows":3,
			}),
		}

class AsstForm(forms.ModelForm):
	class Meta:
		model = AssignmentSt
		fields = ["san","ssubject","scrted","sactive"]
		widgets = {
		"san":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"ssubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"scrted":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			"readonly":True,
			}),
		"sactive":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class SsubForm(forms.ModelForm):
	class Meta:
		model = AssignmentSt
		fields = ["san","ssubject","scrted","sarev"]
		widgets={
		"san":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"ssubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"scrted":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			"readonly":True,
			}),
		"sarev":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Review for Assignment",
			}),
		}

class TsForm(forms.ModelForm):
	class Meta:
		model = AssignmentSt
		fields= ["san","ssubject","scrted","ssubd","sarev","sastre","samarks","stactive"]
		widgets = {
		"san":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"ssubject":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"scrted":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			"readonly":True,
			}),
		"ssubd":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			"readonly":True,
			}),
		"sarev":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"sastre":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Review for Student Assignment",
			}),
		"samarks":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		"stactive":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}

class AdrolU(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","eid","role_type"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"role_type":forms.NumberInput(attrs={
			"class":"form-control my-2",
			})
		}

class UsplForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","eid","first_name","last_name","email","upfe"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Emailid",
			}),
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"eid":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		}

class ChgPwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm New Password"}))
	class Meta:
		model = User
		fields = ["old_password","new_password1","new_password2"]

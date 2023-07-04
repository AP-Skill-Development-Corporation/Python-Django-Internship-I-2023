from django import forms
from . models import User,TeacherProfile,StudentProfile
from django.contrib.auth.forms import UserCreationForm

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
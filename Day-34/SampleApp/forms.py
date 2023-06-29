from .models import Student
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['sroll','sname','syear','sbranch',"sage"]
		widgets = {
		"sroll":forms.TextInput(attrs={
			'class':"form-control my-1",
			'placeholder':'Enter Roll Number',
			}),
		"sname":forms.TextInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Student Name",
			}),
		"syear":forms.Select(attrs={
			'class':"form-control my-1",
			}),
		"sbranch":forms.Select(attrs={
			'class':"form-control my-1",
			}),
		"sage":forms.NumberInput(attrs={
			'class':"form-control my-1",
			'placeholder':"Enter Age",
			'min':18,
			'max':30,
			}),
		}

class RegForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username"
			}),
		}
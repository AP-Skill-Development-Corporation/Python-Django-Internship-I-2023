from django import forms
from . models import User,TeacherProfile
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
		fields = '__all__'
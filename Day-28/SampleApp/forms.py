from .models import Student
from django import forms

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
			'placeholder':"Enter Studnet Name",
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

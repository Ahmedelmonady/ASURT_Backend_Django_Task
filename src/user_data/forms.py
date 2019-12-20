from django import forms

from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'Name',
			'Email',
			'Phone',
			'Age',
			'Gender'
		]
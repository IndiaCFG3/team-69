from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User

class UserRegisterForm(UserCreationForm):
	email 		= forms.EmailField(help_text='Email Id used for registration cannot be changed later.')

	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['email', 'contact', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model 	= User
		fields 	= ['contact']
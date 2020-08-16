from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User

class UserRegisterForm(UserCreationForm):
	email 		= forms.EmailField()
	name 		= forms.CharField(max_length=20)
	age 		= forms.IntegerField(min_value=0)
	date_of_birth = forms.DateField(help_text='YYYY-MM-DD Format')
	income		= forms.IntegerField(min_value=0)
	family_size = forms.IntegerField(min_value=1)
	location 	= forms.CharField(max_length=120)

	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'age', 'date_of_birth', 'income', 'family_size', 'location', 'contact', 'password1', 'password2']
	
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

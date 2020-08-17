from django import forms
from .models import Document

class DocumentsUpdateForm(forms.ModelForm):
	class Meta:
		model 	= Document
		fields 	= ['aadhar_card', 'driving_license', 'voter_id', 'birth_certificate', 'pan_card', 'ration_card']

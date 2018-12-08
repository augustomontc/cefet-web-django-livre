from django import forms
from .models import Pastel, Recheio
from django.forms import ModelForm

class PastelForm(forms.ModelForm):
	recheio = forms.ModelChoiceField(queryset=Recheio.objects.all().order_by('nome'), empty_label="Escolha...")
	
	class Meta:
		model = Pastel
		fields = '__all__'
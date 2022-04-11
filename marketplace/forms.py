from django import forms

from .models import Product, Buyer


class BuyerForm(forms.ModelForm):
	class Meta:
		model = Buyer
		fields = '__all__'
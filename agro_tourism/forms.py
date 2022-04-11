from django import forms
from django.forms import inlineformset_factory

from .models import Farm, Package

class PackageForm(forms.ModelForm):

	class Meta():
		model = Package
		fields = '__all__'


FarmFormSet = inlineformset_factory(Farm, Package,
                                            form=PackageForm, extra=1)

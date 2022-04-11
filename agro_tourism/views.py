from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import reverse, redirect
from django.views.generic.edit import CreateView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Farm, Package, BookPackage
from .forms import FarmFormSet

class FarmPackageCreateView(LoginRequiredMixin, CreateView):
	model = Farm
	form = FarmFormSet
	template_name = 'agro-tourism/farm_package_create.html'
	fields = ['name', 'owner', 'location', 'area', 'contact', 'features', 'images']

	def get_context_data(self, **kwargs):
		data = super(FarmPackageCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
		    data['farm_section'] = FarmFormSet(self.request.POST, self.request.FILES)
		else:
			data['farm_section'] = FarmFormSet()

		return data

	def form_valid(self, form):
		context = self.get_context_data()
		farm_section = context['farm_section']

		with transaction.atomic():
			self.object = form.save()
			if farm_section.is_valid():
				farm_section.instance = self.object
				farm_section.save()
		return super(FarmPackageCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('home')


def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'agro-tourism/farm_list.html', {'farms': farms})


def package_list(request):
    packages = Package.objects.all()
    return render(request, 'agro-tourism/package_list.html', {'packages': packages})


def farm_details(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    packages = Package.objects.filter(pk=farm.pk)
    return render(request, 'agro-tourism/farm_details.html', {'farm': farm, 'packages': packages})


class BookPackageCreateView(CreateView):
	model = BookPackage
	template_name = 'agro-tourism/book_package.html'
	fields = '__all__'
	success_url = 'marketplace'
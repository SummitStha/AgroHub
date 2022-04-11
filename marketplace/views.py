from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import Buyer, Product, RequestProduct


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'marketplace/product_create.html'
    model = Product
    success_url = '/marketplace'
    fields = ['name', 'location', 'quantity', 'cost',
              'description', 'supplier', 'contact', 'image']

    def get_initial(self):
        initial = super(ProductCreateView, self).get_initial()

        initial['supplier'] = self.request.user

        return initial
    


class ProductListView(ListView):
    template_name = 'marketplace/product_list.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(publish = True)
        return context

class BuyerFormCreateView(LoginRequiredMixin, CreateView):
    template_name = 'marketplace/buyer_create.html'
    model = Buyer
    fields = '__all__'
    success_url = 'buyer-list'

    def get_initial(self):
        initial = super(BuyerFormCreateView, self).get_initial()

        initial['buyer'] = self.request.user

        return initial
    
class BuyerListView(ListView):
    template_name = 'marketplace/buyer_list.html'
    model = Buyer

    def get_context_data(self, **kwargs):
        context = super(BuyerListView, self).get_context_data(**kwargs)
        context['data'] = Buyer.objects.filter(buyer = self.request.user)
        return context

class SellingListView(ListView):
    template_name = 'marketplace/selling_list.html'
    model = Buyer

    def get_context_data(self, **kwargs):
        context = super(SellingListView, self).get_context_data(**kwargs)
        context['data'] = Product.objects.filter(supplier = self.request.user)
        return context


class RequestProductView(LoginRequiredMixin, CreateView):
    template_name = 'marketplace/product_request_create.html'
    model = RequestProduct
    fields = '__all__'

    def get_initial(self):
        initial = super(RequestProductView, self).get_initial()

        initial['buyer'] = self.request.user

        return initial
    

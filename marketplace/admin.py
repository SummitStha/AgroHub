from django.contrib import admin

from .models import Buyer, Product, RequestProduct

admin.site.register(Buyer)

admin.site.register(Product)

admin.site.register(RequestProduct)

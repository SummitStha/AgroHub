from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length = 250)
    quantity = models.IntegerField()
    cost = models.DecimalField(
        max_digits=7, decimal_places=2, help_text='cost per unit')
    description = models.TextField()
    supplier = models.ForeignKey(User)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return 'Product Name: {}'.format(self.name)


class Buyer(models.Model):
    buyer = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return 'Buyer: {} Product: {}'.format(self.buyer, self.product)


class RequestProduct(models.Model):
    buyer = models.ForeignKey(User)
    product = models.CharField(max_length=150)
    quantity = models.IntegerField()
    location = models.CharField(max_length = 250)

    def __str__(self):
        return 'Buyer: {}, Product: {}'.format(self.buyer, self.product)

from django.db import models

# Create your models here.


class Farm(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length = 250)
    area = models.DecimalField(max_digits=7, decimal_places=3)
    contact = models.IntegerField()
    features = models.TextField()
    images = models.ImageField(upload_to='farm_image/')
    publish = models.BooleanField(default = False)

    def __str__(self):
        return "Farm: {} location: {}".format(self.name, self.location)


class Package(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    features = models.TextField()
    pricing = models.DecimalField(max_digits=7, decimal_places=2)
    images = models.ImageField(upload_to='package/')

    def __str__(self):
        return "Package: {}".format(self.name)


class BookPackage(models.Model):
    package = models.ForeignKey(Package)
    no_visitors = models.PositiveIntegerField()
    date = models.DateField()
    duration = models.CharField(max_length = 200)
    contact = models.PositiveIntegerField()

    def __str__(self):
        return 'Package: {}'.format(self.package)
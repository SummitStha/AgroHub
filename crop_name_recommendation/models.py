from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
      #p_id = models.IntegerField('p_id')
      first_name = models.CharField(max_length=200)
      last_name = models.CharField(max_length=200)
      gender = models.CharField(max_length=200)
      user_email = models.CharField(max_length=200)
      user_password = models.CharField(max_length=200)
      def __str__(self):
            return self.user_email


class FarmData(models.Model):
	SOIL_TYPE = (
			('ALLUVIAL SOIL', 'Alluvial Soil'),
          	('SANDY BOULDER SOIL', 'Sandy Boulder Soil'),
          	('RED BROWN SOIL', 'Red Brown Soil'),
          	('LACUSTRINE SOIL', 'Lacustrine Soil'),
          	('GLACIAL SOIL', 'Glacial Soil')
		)

	SEASONS = (
			('SPRING SEASON', 'Spring Season'),
			('SUMMER SEASON', 'Summer Season'),
			('MONSOON SEASON', 'Monsoon Season'),
			('AUTUMN SEASON','Autumn Season'),
			('WINTER SEASON', 'Winter Season')
		)

	area = models.CharField(max_length = 200)
	recorded_date = models.DateTimeField(auto_now_add=True)
	soil_type = models.CharField(max_length=100, choices=SOIL_TYPE)
	soil_depth = models.DecimalField(max_digits = 7, decimal_places = 2, help_text = 'Soil depth (in cms)')
	ph = models.DecimalField(max_digits = 2, decimal_places = 2, help_text = 'pH value of the soil')
	bulk_density = models.DecimalField(max_digits = 7, decimal_places=2, help_text = 'Bulk Density of the soil (in gm/cc)')
	electrical_conductivity = models.DecimalField(max_digits = 5, decimal_places=2, help_text='Levels of electrical conductivity ')
	organic_carbon_percentage = models.DecimalField(max_digits = 5, decimal_places=2, help_text='Organic Carbon in soil (in %) ')
	soil_moisture_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, help_text = 'Soil Moisture Retention (in %)')	
	available_water_capacity = models.DecimalField(max_digits = 7, decimal_places=2, help_text='Water tank capacity for the irrigation(in cms)')
	infiltration_rate = models.DecimalField(max_digits = 7, decimal_places=2, help_text='Infiltration rate ( in cm/hr)')
	clay_percent = models.DecimalField(max_digits = 5, decimal_places=2, help_text='Percentage of clay in the soil (in %)')
	recorded_season = models.CharField(max_length = 100, choices=SEASONS)

	def __str__(self):
		return 'Area: {} Recorded Date: {}'.format(self.area, self.recorded_date)




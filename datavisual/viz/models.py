# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
Premium_Choices = (
	('enterpirse_data.venues_basic', 'BASIC'),
	('enterpirse_data.venues_premium', 'PREMIUM'),
	('enterpirse_data.venues_rich', 'RICH')
	)

Cat_Choices = (
	('Arts & Entertainment', 'ARTS'),
	('Colleges & Universities', 'COLLEGE'),
	('Events', 'EVENTS'),
	('Food', 'FOOD'),
	('Nightlife Spots', 'NIGHTLIFE'),
	('Outdoors & Recreation', 'OUTDOORS'),
	('Professional & Other Places', 'PROFESSIONAL'),
	('Residences', 'RESIDENCES'), 
	('Shops & Services', 'SHOPS'),
	('Travel & Transport', 'TRAVEL')
		)
	



class Enterpise_Data(models.Model):
	tables = models.CharField(max_length=40, choices=Premium_Choices, default = 'BASIC')
	cats = models.CharField(max_length = 80, choices=Cat_Choices, null = True)


	


	'''def __str__(self):
		return self.table'''

'''class State(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name
'''



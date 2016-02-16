from __future__ import unicode_literals

from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class DataSet(models.Model):
	name = models.CharField(max_length=200)
	csv = models.FileField(null=True,blank=True)

	def __str__(self):
		return self.name

class QuantitativeVariable(models.Model):
	name = models.CharField(max_length=200)
	dataset = models.ForeignKey(DataSet,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class QualitativeVariable(models.Model):
	name = models.CharField(max_length=200)
	dataset = models.ForeignKey(DataSet,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)
	color = models.CharField(max_length=10)
	variable = models.ForeignKey(QualitativeVariable, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Breakpoint(models.Model):
	minimum = models.IntegerField()
	maximum = models.IntegerField()
	color = ColorField(blank=True, default='#FFFFFF')
	variable = models.ForeignKey(QuantitativeVariable,on_delete=models.CASCADE)

	def __str__(self):
		return self.color

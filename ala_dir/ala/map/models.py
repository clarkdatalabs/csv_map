from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DataSet(models.Model):
	name = models.CharField(max_length=200)
	csv = models.FileField(null=True,blank=True)

	def __str__(self):
		return self.name

class Variable(models.Model):
	name = models.CharField(max_length=200)
	dataset = models.ForeignKey(DataSet,on_delete=models.CASCADE)

class Breakpoint(models.Model):
	minimum = models.IntegerField()
	maximum = models.IntegerField()
	color = models.CharField(max_length=10)
	variable = models.ForeignKey(Variable,on_delete=models.CASCADE)

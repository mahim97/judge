from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class question(models.Model):
	prob_code=models.CharField('Problem Code',max_length=40, primary_key=True)
	prob_statement=models.CharField('Problem Statement',max_length=2000)
	inp=models.CharField('Input',max_length=2000)
	out=models.CharField('Output',max_length=2000)
	constra=models.CharField('Constraints',max_length=2000)
	eg=models.CharField('Example',max_length=2000)
	sub=models.IntegerField('Successful Submission',default=0)
	author=models.CharField(max_length=2000)
	def __str__(self):
		return self.prob_code
	
@python_2_unicode_compatible
class queslist(models.Model):
	name=models.CharField(max_length=30)
	sub=models.IntegerField('Successful Submission',default=0)
	def __str__(self):
		return self.name
	

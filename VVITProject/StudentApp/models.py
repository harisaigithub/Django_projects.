from django.db import models

# Create your models here.
class StReg(models.Model):
	c = [
		('0','--Select Branch--'),
		('1','CSE'),
		('2','CSM'),
		('3','CSO'),
		('4','IT'),
		('5','Other'),
	]
	srn = models.CharField(max_length=10)
	sname = models.CharField(max_length=150)
	syear = models.IntegerField(default=1)
	sbranch = models.CharField(choices=c, max_length=5, default='0')
	def __str__(self):
		return self.srn+" "+self.sname
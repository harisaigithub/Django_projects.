from django.db import models

# Create your models here.
class Emp(models.Model):
	k = [
		('0','-- Select Designation --'),
		('1','Intern'),
		('2','Junior Trainee'),
		('3','Junior Developer'),
		('4','Other')
	]
	eid = models.CharField(max_length=5)
	ename = models.CharField(max_length=150)
	eage = models.IntegerField(default=20)
	esal = models.IntegerField()
	edesg = models.CharField(choices=k,max_length=10,default='0')
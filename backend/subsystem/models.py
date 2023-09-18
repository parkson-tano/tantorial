from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Subsystem(models.Model):
	title = models.CharField(max_length=26)

	def __str__(self):
		return self.title

class Language(models.Model):
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class ClassRoom(models.Model):
	school = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='school_classroom')
	subsystem = models.ForeignKey(Subsystem, null=True, blank=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class Subject(models.Model):
	school = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='school_subject')
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
	
class Country(models.Model):
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
	
class Region(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
	
class Division(models.Model):
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
	
class SubDivision(models.Model):
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
	
class Locality(models.Model):
	subdivision = models.ForeignKey(SubDivision, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
from django.db import models
# Create your models here.

class Subsystem(models.Model):
	title = models.CharField(max_length=26)

	def __str__(self):
		return self.title

class Language(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class Cycle(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class ClassRoom(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class Subject(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
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
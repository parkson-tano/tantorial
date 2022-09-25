from django.db import models

# Create your models here.

class Subsystem(models.Model):
	title = models.CharField(max_length=26)

	def __str__(self):
		return self.title

class ClassRoom(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title

class Subject(models.Model):
	subsystem = models.ForeignKey(Subsystem, on_delete=models.CASCADE)
	title = models.CharField(max_length=56)

	def __str__(self):
		return self.title
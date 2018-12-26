from django.db import models

# Create your models here.
class Job(models.Model):
	Image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)
	name = models.CharField(max_length=64, default='xxx')
	year = models.IntegerField(default=2018)
	role = models.CharField(max_length=100, default='xxx')

	def __str__(self):
		return self.name
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Login(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=144)

	def __unicode__(self):
		return '/%s/' % self.name

	def get_absolute_url(self):
		return '/login/%s/' % self.id 

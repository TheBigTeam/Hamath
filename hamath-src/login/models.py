from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Login(models.Model):
	first_name = models.CharField(max_length=30, default='first name', null=False)
	last_name = models.CharField(max_length=30, default='last name', null=False)

	email = models.EmailField(max_length=50,  default='email@website.com', null=False)
	password = models.CharField(max_length=144)

	date = models.DateTimeField(default=timezone.now)

	def get_full_name(self):
		full_name = self.first_name + " " + self.last_name
		return full_name

	'''
	/mydomain/login/user_id
	queries db with id
	'''
	def get_absolute_url(self):
		return '/video/%s' % self.id

	'''
	display title in /admin/login/login
	'''
	def __unicode__(self):
		return '%s' % self.get_full_name()


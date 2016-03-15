from __future__ import unicode_literals
from django.db import models
from game.models import RookieScore
from game.models import IntermediateScore
from game.models import MasterScore

class Student(models.Model):
	username = models.CharField(max_length=50, null=True)
	first_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	
	rookie_score = models.ForeignKey('game.RookieScore')
	intermidate_score = models.ForeignKey('game.IntermediateScore')
	master_score = models.ForeignKey('game.MasterScore')

	def get_full_name(self):
		full_name = self.first_name + " " + self.last_name
		return full_name

	def __unicode__(self):
		return '%s' % self.get_full_name()
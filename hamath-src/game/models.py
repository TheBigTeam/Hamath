from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class RookieScore(models.Model):
	rookie_mode_score = models.DecimalField(max_digits=2, decimal_places=0, default=Decimal('0'))

	def __unicode__(self):
		return '%s' % self.rookie_mode_score


class IntermediateScore(models.Model):
	intermediate_mode_score = models.DecimalField(max_digits=2, decimal_places=0, default=Decimal('0'))
	
	def __unicode__(self):
		return '%s' % self.intermediate_mode_score

 
class MasterScore(models.Model):
	master_mode_score = models.DecimalField(max_digits=2, decimal_places=0, default=Decimal('0'))

	def __unicode__(self):
		return '%s' % self.master_mode_score

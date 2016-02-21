from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Score(models.Model):
	rookie_mode_score = models.CharField(max_length=200, null=True)
	intermediate_mode_score = models.CharField(max_length=200, null=True)
	master_mode_score = models.CharField(max_length=200, null=True)
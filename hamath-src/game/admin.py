from django.contrib import admin
from game.models import RookieScore, IntermediateScore, MasterScore

admin.site.register(RookieScore)
admin.site.register(IntermediateScore)
admin.site.register(MasterScore)
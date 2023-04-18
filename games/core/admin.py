from django.contrib import admin

from .models import Game, Team

admin.site.register(Team)
admin.site.register(Game)
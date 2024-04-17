from django.contrib import admin
from .models import Stadium, Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ["team_name", "home_ground"]

admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium)
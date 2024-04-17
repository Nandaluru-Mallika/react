from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Stadium, Team
from django.views import View

# Create your views here.
class StadiumsView(ListView):
    template_name = "info/stadiums.html"
    model = Stadium
    context_object_name = "stadiums"

class StadiumDetailView(DetailView):
    template_name = "info/stadium_detail.html"
    model = Stadium

class TeamsView(ListView):
    template_name = "info/teams.html"
    model = Team
    context_object_name = "teams"

class TeamDeatilView(View):
    def get(self, request, pk):
        team = Team.objects.get(pk=pk)
        team_name = team.team_name
        team_members = team.team_members.split(',')
        return render(request, "info/team_detail.html", {
            "team_name": team_name,
            "team_members": team_members,
            "home_ground": team.home_ground,
            "home_ground_id": team.home_ground.pk
        })

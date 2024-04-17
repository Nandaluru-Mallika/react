from django.urls import path
from . import views

urlpatterns = [
    path("stadiums", views.StadiumsView.as_view(), name="stadiums"),
    path("stadiums/<int:pk>", views.StadiumDetailView.as_view(), name="stadium_detail"),
    path("teams", views.TeamsView.as_view(), name="teams"),
    path("teams/<int:pk>", views.TeamDeatilView.as_view(), name="team_detail")
]

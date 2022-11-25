from django.urls import path
from .views import TeamsView, TeamDetailView

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<team_id>/", TeamDetailView.as_view())
]
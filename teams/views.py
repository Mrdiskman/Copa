from rest_framework.views import APIView, Request, Response
from django.forms.models import model_to_dict
from .models import Team

class TeamsView(APIView):
    def get(self, req:Request) -> Response:
        teams = Team.objects.all()
        teams_list = []
        for team in teams:
            teams_dict = model_to_dict(team)
            teams_list.append(teams_dict)
        return Response(teams_list)

    def post(self, req:Request) -> Response:

        team = Team.objects.create(**req.data)
        teams_dict = model_to_dict(team)
        return Response(teams_dict, 201)
    
class TeamDetailView(APIView):
    def get(self, req:Request, team_id:int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist: 
            return Response({'message': 'Team not found'}, 404)
        team_dict = model_to_dict(team)
        return Response(team_dict)

    def patch(self, req:Request, team_id:int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist: 
            return Response({'message': 'Team not found'}, 404)
        for key, value in req.data.items():
            setattr(team, key, value)
        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, 200)
    
    def delete(self, req:Request, team_id:int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist: 
            return Response({'message': 'Team not found'}, 404)
        team.delete()
        return Response(status=204)
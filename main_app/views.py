from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# from nba_api.stats.endpoints import playercareerstats
# from django.http import JsonResponse

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

# def playerstats(request):
#     dfs = playercareerstats.PlayerCareerStats(
#             player_id="2544", per_mode36="PerGame", league_id_nullable="00"
# ).get_data_frames()[0]
#     return JsonResponse(dfs, safe=False)
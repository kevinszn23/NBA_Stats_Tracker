from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from nba_api.stats.endpoints import playercareerstats
# from django.http import JsonResponse
import requests
from main_app.models import Player
# import sys
import json

# Create your views here.
# class Home(DetailView):
#     model = Player
#     template_name = "home.html"

    # def nba_api_test(request):
    #     dfs = playercareerstats.PlayerCareerStats(
    #             player_id="2544", per_mode36="PerGame", league_id_nullable="00"
    # ).get_data_frames()[0]
    #     print(f"{dfs}")

    #     lcs = dfs.iloc[19]
    #     print(f"{lcs}")
    #     return render(request, "home.html")

    # def balldontlie(self):
    #     response = requests.get("https://www.balldontlie.io/api/v1/players/237")
    #     data = response.json()
    #     return data["disclaimer"]

    # def get_context_data(self, *args, **kwargs):
    #     context = super(Home, self).get_context_data(*args, **kwargs)
    #     context['base'] = self.balldontlie()
    #     return context

# def index(request):
#     response=requests.get("https://stats.nba.com/stats/playercareerstats?LeagueID=&PerMode=Totals&PlayerID=2544").json()
#     return render(request,'index.html',{'response':response})


# def home(request):
#     all_players = {}
#     all_players_url = "https://stats.nba.com/stats/playercareerstats?LeagueID=&PerMode=Totals&PlayerID=2544"
#     response_all_players = requests.get(all_players_url)
#     temp_all_players = response_all_players.json()
#     result_all_players = temp_all_players['data']

#     for i in result_all_players:
#         player_data = Player(
#             player_id = i['id'],
#             first_name = i['first_name'],
#             last_name = i['last_name']
#         )
#         player_data.save()
#     all_players = Player.objects.all().order_by('-id')
#     return render(request, "home.html", {"all_players": all_players})

# nba = "https://stats.nba.com/stats/playercareerstats?LeagueID=&PerMode=Totals&PlayerID=2544"

# # "https://stats.nba.com/stats/playercareerstats"

# print(requests.get(nba).content)

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from nba_api.stats.endpoints import playercareerstats
# from django.http import JsonResponse
import requests
from main_app.models import Player
# import sys

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    model = Player

    # def nba_api_test(request):
    #     dfs = playercareerstats.PlayerCareerStats(
    #             player_id="2544", per_mode36="PerGame", league_id_nullable="00"
    # ).get_data_frames()[0]
    #     print(f"{dfs}")

    #     lcs = dfs.iloc[19]
    #     print(f"{lcs}")
    #     return render(request, "home.html")
    
    def balldontdie(request):
        requests.get("https://www.balldontlie.io/api/v1/players/237")
        data = response.json()
        return render(request, "home.html", {
            "nba": data["display"]
        })


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

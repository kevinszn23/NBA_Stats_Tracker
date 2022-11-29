from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# from nba_api.stats.endpoints import playercareerstats
# from django.http import JsonResponse
import requests
from main_app.models import Player

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

def show_page(request):
    all_players = {}
    all_players_url = "https://stats.nba.com/stats/playercareerstats"
    response_all_players = requests.get(all_players_url)
    temp_all_players = response_all_players.json()
    result_all_players = temp_all_players['data']

    for i in result_all_players:
        player_data = Player(
            player_id = i['id'],
            first_name = i['first_name'],
            last_name = i['last_name']
        )
        player_data.save()
    all_players = Player.objects.all().order_by('-id')
    return render(request, "show_page.html", {"all_players": result_all_players})
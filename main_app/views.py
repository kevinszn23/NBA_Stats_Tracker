from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from nba_api.stats.endpoints import playercareerstats

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"



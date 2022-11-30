from django.urls import path
from . import views

urlpatterns = [
    # path("<slug:slug>/", views.Home.as_view(), name="home"),
    path('',views.index,name="index")

]
from nba_api.stats.static import players

player_dict = players.get_players()
print(f"{player_dict}")
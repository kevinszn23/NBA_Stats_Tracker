from nba_api.stats.static import players

player_dict = players.get_players()
# print(f"{player_dict}")

lebron = [player for player in player_dict if player["full_name"] == "LeBron James"][0]
print(f"{lebron}")
lebron_id = lebron["id"]
print(f"{lebron_id}")
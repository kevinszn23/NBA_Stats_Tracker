from nba_api.stats.static import players

player_dict = players.get_players()
# print(f"{player_dict}")

lebron = [player for player in player_dict if player["full_name"] == "LeBron James"][0]
print(f"{lebron}")

lebron_id = lebron["id"]
print(f"{lebron_id}")

from nba_api.stats.static import teams

team_dict = teams.get_teams()
# print(f"{team_dict}")

gsw = [team for team in team_dict if team["full_name"] == "Golden State Warriors"][0]
print(f"{gsw}")

gsw_id = gsw["id"]
print(f"{gsw_id}")
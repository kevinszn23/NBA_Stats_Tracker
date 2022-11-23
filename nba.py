import pandas as pd

from nba_api.stats.static import players

player_dict = players.get_players()
# print(f"{player_dict}")

# lebron = [player for player in player_dict if player["full_name"] == "LeBron James"][0]
# print(f"{lebron}")

# lebron_id = lebron["id"]
# print(f"{lebron_id}")

# from nba_api.stats.static import teams

# team_dict = teams.get_teams()
# # print(f"{team_dict}")

# gsw = [team for team in team_dict if team["full_name"] == "Golden State Warriors"][0]
# print(f"{gsw}")

# gsw_id = gsw["id"]
# print(f"{gsw_id}")

# from nba_api.stats.endpoints import playergamelog

# gamelog_lebron = playergamelog.PlayerGameLog(player_id="2544")
# gamelog_lebron_df = gamelog_lebron.get_data_frames()[0]
# print(f"{gamelog_lebron_df}")

from nba_api.stats.endpoints import playercareerstats

# ppg = playercareerstats.PlayerCareerStats(player_id="2544")
# ppg.get_data_frames()[0]
# ppg.get_json()
# ppg.get_dict()
# print(f"{ppg.get_data_frames()[0]}")

# ppg2 = playercareerstats.PlayerCareerStats(player_id="2544")
# print(f"{ppg2.season_totals_regular_season.get_data_frame()}")

# career averages
# dfs = playercareerstats.PlayerCareerStats(
#             player_id="2544", per_mode36="PerGame"
# ).get_data_frames()[1]
# print(f"{dfs}")

# season averages
dfs = playercareerstats.PlayerCareerStats(
            player_id="2544", per_mode36="PerGame", league_id_nullable="00"
).get_data_frames()[0]
print(f"{dfs}")

lcs = dfs.iloc[19]
print(f"{lcs}")
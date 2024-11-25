import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
import numpy as np
import plotly.express as px
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, teamgamelog, playergamelog, boxscoretraditionalv2, leaguegamefinder, LeagueGameFinder, playbyplayv2

def player_stats(player_name):
    player = players.find_players_by_full_name(player_name)[0]
    player_id = player['id']
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season='2024-25', season_type_all_star='Regular Season')
    game_log_df = game_log.get_data_frames()[0]
    

    # Print the game log
    return game_log_df
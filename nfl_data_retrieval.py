import pandas as pd 
import constants
import sqlite3

# Returns full play-by-play data for a given season
# Season should be passed in as an integer
# Includes regular and postseason games
def get_league_play_by_play_data(season):
    base_url = 'https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_' + str(season) + '.csv.gz'
    pbp_data = pd.read_csv(base_url, compression='gzip', low_memory=False)
    pbp_data = pbp_data[constants.pbp_filter_list]
    output_file = f"raw_pbp_data/{season}_NFL.csv"
    pbp_data.to_csv(output_file, index=False)
    return pbp_data

# Returns offensive stats for all players in a given season 
# Season should be passed in as an integer
# Includes regular, postseason, and reg+post combined stats
def get_offensive_player_stats(season):
    base_url = 'https://github.com/nflverse/nflverse-data/releases/download/player_stats/player_stats_season_' + str(season) + '.csv'
    player_stats = pd.read_csv(base_url, low_memory=False)
    output_file = f"raw_player_stats/{season}_NFL.csv"
    player_stats.to_csv(output_file, index=False)
    return player_stats

if __name__ == "__main__":
    try:
        db_conn = sqlite3.connect("nfl_stats.db")
        
        pbp_df = get_league_play_by_play_data(2024)
        pbp_df.to_sql('pbp_2024', db_conn, if_exists='replace', index=False)

        player_stats_season_df = get_offensive_player_stats(2024)
        player_stats_season_df.to_sql('player_stats_season_2024', db_conn, if_exists='replace', index=False)
    finally:
        db_conn.close()

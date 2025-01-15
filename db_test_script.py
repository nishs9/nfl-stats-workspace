import sqlite3
import pandas as pd
from constants import pbp_filter_list

if __name__ == "__main__":
    db_conn = sqlite3.connect("nfl_stats.db")
    db_conn.row_factory = sqlite3.Row
    cursor = db_conn.cursor()
    query_result = cursor.execute("select * from pbp_2024 limit 10")
    query_result_df = pd.DataFrame(query_result.fetchall(), columns=pbp_filter_list)
    print(query_result_df.head())
    for row in query_result.fetchall():
        print(row["game_id"])
# nfl-stats-workspace
This is an unorganized repo where I store scripts for various side projects. Most of the scripts in here are related to NFL stats and I will periodically update the README with info on what all lives in the repo.

## NFL Stats DB with SQLite
Using `nfl_data_retrieval.py` you can set up a local database with NFL player stats and play-by-play data from 2024 in minutes. The data itself is courtesy of nflverse. You can check out the full data repo here: [https://github.com/nflverse/nflverse-data/releases](https://github.com/nflverse/nflverse-data/releases).

In order to set up the database, start by cloning the repo and setting up the python virtual environment:

```
git clone *repo url*
cd nfl-stats-workspace
python3 -m venv nfl-stats-workspace
source nfl-stats-workspace/bin/activate
```

Next, install the necessary dependencies from the `requirements.txt` file and create the database for the stats:

```
pip install -r requirements.txt
sqlite3 nfl_stats.db
```

Verify that the db was created successfully and then you can run the data retrieval script to populate the database

```
python nfl_data_retrieval.py
```

The script will create 2 tables within `nfl_stats.db`: `pbp_2024` and `player_stats_season_2024`
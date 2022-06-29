import numpy as np
import pandas as pd

from nba_api.stats.endpoints import boxscoreplayertrackv2
from nba_api.stats.endpoints import leaguegamelog
import time

start = time.time()

#Create List of games
games = leaguegamelog.LeagueGameLog(season='2019-20').get_data_frames()[0]
games = games['GAME_ID'].unique()


#Get tracking stats per game
df = pd.DataFrame()
for index in games:
    raw = boxscoreplayertrackv2.BoxScorePlayerTrackV2(index).get_data_frames()[0]
    df = df.append(raw)

df.to_csv('final_df.csv')
print("--- %s seconds ---" % (time.time() - start))

import numpy as numpy
import pandas as pd 
from sqlalchemy import create_engine
import sqlite3
conn = sqlite3.connect('features.db')
#new_conn = 
engine = create_engine("sqlite://", echo=False)

features_db = pd.read_csv('fma_metadata/features.csv', index_col = 0, header = [0,1,2])
tracks_db = pd.read_csv('fma_metadata/tracks.csv', index_col = 0, header = [0,1])
#features_db = pd.read_pickle('features.pkl')
features_db.columns = [''.join(col).strip() for col in features_db.columns.values]
tracks_db.columns = [''.join(col).strip() for col in tracks_db.columns.values]
final_db = pd.merge(features_db, tracks_db[['trackgenre_top']], on = 'track_id', how = 'left')
#final_db.rename(index={0: "track_id"})

final_db.to_csv('make_db.csv')




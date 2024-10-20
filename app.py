# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:10:37 2024

@author: Swapnil Mishra
"""

from flask import Flask, render_template, request
import pandas as pd
import joblib
from sqlalchemy import create_engine
import psycopg2  # PostgreSQL connector

app = Flask(__name__)

# Connect to PostgreSQL
con = psycopg2.connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='swapnil1989',
    dbname='recommenddb'
)

cur = con.cursor()
con.commit()

cur.execute('SELECT * FROM anime')
df = cur.fetchall()

anime = pd.DataFrame(df)

anime = anime.rename({0: 'anime_id'}, axis=1)
anime = anime.rename({1: 'name'}, axis=1)
anime = anime.rename({2: 'genre'}, axis=1)
anime = anime.rename({3: 'type'}, axis=1)
anime = anime.rename({4: 'episodes'}, axis=1)
anime = anime.rename({5: 'rating'}, axis=1)
anime = anime.rename({6: 'members'}, axis=1)

anime["genre"] = anime["genre"].fillna(" ")

tfidf = joblib.load('matrix')
tfidf_matrix = tfidf.transform(anime.genre)

cosine_sim_matrix = joblib.load('cosine_matrix')

anime_index = pd.Series(anime.index, index=anime['name']).drop_duplicates()

### Custom Function ###
def get_recommendations(Name, topN):
    anime_id = anime_index[Name]
    
    cosine_scores = list(enumerate(cosine_sim_matrix[anime_id]))
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1], reverse=True)
    cosine_scores_N = cosine_scores[0:topN+1]
    
    anime_idx = [i[0] for i in cosine_scores_N]
    anime_scores = [i[1] for i in cosine_scores_N]
    
    anime_similar_show = pd.DataFrame(columns=["name", "Score"])
    anime_similar_show["name"] = anime.loc[anime_idx, "name"]
    anime_similar_show["Score"] = anime_scores
    anime_similar_show.reset_index(inplace=True)
    
    return anime_similar_show.iloc[1:, ]

######End of the Custom Function######    

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guest', methods=["POST"])
def Guest():
    if request.method == 'POST':
        mn = request.form["mn"]
        tp = request.form["tp"]
        
        q = get_recommendations(mn, topN=int(tp))
        
        # Connection to PostgreSQL database
        engine = create_engine(f"postgresql://postgres:swapnil1989@localhost:5432/recommenddb")
        
        # Transfering the file into a database
        q.to_sql('top_10', con=engine, if_exists='replace', chunksize=1000, index=False)
        
        return render_template("data.html", Y="Results have been saved in your database", Z=q.to_html())

if __name__ == '__main__':
    app.run(debug=True)

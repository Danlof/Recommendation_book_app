import pandas as pd
import numpy as np

import joblib
import requests

FILTERD_BOOKS = '/media/danlof/dan files/data_science_codes/Recommender_project/books_data/filtered_books.pkl'
SIM_MATRIX = '/media/danlof/dan files/data_science_codes/Recommender_project/books_data/similarity_matrix.pkl'

books_df = pd.read_csv(FILTERD_BOOKS)
sim_matrix = joblib.load(SIM_MATRIX)

def get_top_n_books():
    """This function returns the top n popular books recommended """
    df = books_df.sort_values(by=['Rating_count','Avg_rating'],ascending=False).head(n)
    return df

def recommendation_by_id(book_id):
    try:
        recomm_books = pd.DataFrame(sim_matrix[book_id].sort_values(ascending = True).head(10)).reset_index()[1:]
        recomm_df = pd.DataFrame(columns=books_df.columns)
        for title in recomm_books['Title']:
            recomm = books_df[books_df['Title']==title]
            recom_df = pd.concat([recomm_df,recomm])
        return recom_df
    except KeyError:
        print("Books not found in the similarity matrix.Please choose another book")

print(recommendation_by_id('1567407781'))
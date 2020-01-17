# Install kaggle api. pip3 install kaggle
import kaggle
import re
import pandas as pd
import time
from datetime import datetime

# Refer video session:
# Create account in https://kaggle.com if you do not have one already
# Download access token from kaggle website and save it as kaggle.json in ~.kaggle directory
# Kaggle API reference - https://github.com/Kaggle/kaggle-api & https://www.kaggle.com/docs/api
# No direct python supporting documents are available. Let us learn how can we explore ourselves

# Choose a data set and describe the use case for this data and jod down the steps that involves to achieve the same
# https://www.kaggle.com/tunguz/movietweetings
# Connect and authenticate Kaggle API
orskl_kaggle = kaggle.KaggleApi()
orskl_kaggle.authenticate()
orskl_dataset_loc = 'tunguz/movietweetings'
orskl_dataset = orskl_kaggle.dataset_view(orskl_dataset_loc)
orskl_dataset.files

# Pull data files from this datasets
# orskl_kaggle.dataset_download_cli(orskl_dataset_loc, unzip=True)

# Understand three data files
# movies.dat, ratings.dat and users.dat
orskl_ratings_data = pd.read_csv('ratings.dat', header=None,
                                 names=['user_id', 'movie_id', 'rating', 'rating_timestamp'],
                                 sep='::', engine='python')
# Why the default engine = 'c' doesnt work, what happens if we don't use this engine

orskl_movies_data = pd.read_csv('movies.dat', header=None, names=['movie_id', 'movie_title', 'genre'],
                                sep='::', engine='python')

orskl_users_data = pd.read_csv('users.dat', header=None, names=['user_id', 'twitter_id'],
                               sep='::', engine='python')


# Let us extract year from the movie title
# Regex simulator - https://regex101.com/r/5XjNqh/1
def extract_year(x):
    pattern = r"\((.*?\))"
    match = re.search(pattern, x)
    if match is not None:
        return match.group(0).strip("(").strip(")")
    else:
        return None


orskl_movies_data["movie_year"] = orskl_movies_data["movie_title"].apply(lambda movie_title: extract_year(movie_title))

# Find distinct number of genre from movies data
# This is called list comprehension
orskl_genre_list = [x.split("|") for x in orskl_movies_data["genre"].fillna("")]
orskl_genre_flat_list = list(set([item for sublist in orskl_genre_list for item in sublist]))
print(len(orskl_genre_flat_list))
# There are 28 distinct genres in the data, after excluding null element

# Join all the data files and create one data frame
# Keeping ratings data as the primary data, let us add twitter details and movie details
orskl_movies_stage = orskl_ratings_data.join(orskl_movies_data, lsuffix='_rat', rsuffix='_mov', how="left",
                                             on='movie_id')
orskl_final_ratings = orskl_movies_stage.join(orskl_users_data, lsuffix='_usr', rsuffix='_twi', how="left",
                                              on='user_id')

# Analyse data
#   - How many user accounts exists?
print(orskl_final_ratings["user_id_usr"].nunique())
#   - How many movies doesn't have titles?
print(orskl_final_ratings["movie_id_mov"].isnull().sum())
#   - For each movie, what is the count, min, max and average rating?
print(orskl_final_ratings.groupby("movie_title").rating.agg(['min', 'max', 'mean', 'count']).
      reset_index().sort_values('count', ascending=False))
#   - Sort the above stats by count of ratings
print(orskl_final_ratings.groupby("movie_title").rating.agg(['min', 'max', 'mean', 'count']))

# Exercise:
# - Convert rating_timestamp to date
# - For each move, find dates when minimum rating was given and maximum rating

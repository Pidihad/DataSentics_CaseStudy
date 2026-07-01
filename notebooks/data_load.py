"""
Exploratory Analysis

Loads and joins Books, Ratings and Users data.
"""

import pandas as pd
import os

# %% Load data
DATA_PATH = os.path.join(os.path.dirname(__file__), "..","data", "book-recommendation-dataset")

books = pd.read_csv(
    os.path.join(DATA_PATH, "Books.csv"),
    sep=",",
    on_bad_lines="skip",
    encoding="latin-1",
    low_memory=False,
)

ratings = pd.read_csv(
    os.path.join(DATA_PATH, "Ratings.csv"),
    sep=",",
    on_bad_lines="skip",
    encoding="latin-1",
)

users = pd.read_csv(
    os.path.join(DATA_PATH, "Users.csv"),
    sep=",",
    on_bad_lines="skip",
    encoding="latin-1",
)

# %% Join: Ratings as bridge between Books and Users
df = (
    ratings
    .merge(books, on="ISBN", how="inner")
    .merge(users, on="User-ID", how="inner")
)

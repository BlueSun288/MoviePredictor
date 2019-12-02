import pandas as pd
import numpy as np



def runMachine():
    # Iterates through list of movies to determine P(MovieRating == 5 | inputs...) for each movie
    print

def probMovie(index, rt):   # int index: Index of target movie
    # Finds P(MovieRating == 5) for a given movie
    rtLength = len(rt.index)  # Length of ratings dataset
    mRt = rt.loc(254)         # Gets all instances of target movie
    print(mRt["Rating"].values_count())
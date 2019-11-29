# Jack MacCallum & Siddhant Grover
# CS447 Term Project - Movie Predictor
# Takes input from GUI of several movies & ratings and determines
# the probability for each movie in the full data set that a user
# will give it a rating of 5

import pandas as pd
import numpy as np
import predictor




def runMachine():
    # Iterates through list of movies to determine P(MovieRating == 5 | inputs...) for each movie
    for ind in mv.index:
        a = probMovie(ind)
        mv[ind, "P"] = a
        print(ind," ",a)
    print("done")


def probMovie(tgt):   # int ind: Index of target movie
    # Finds P(MovieRating == 5) for a given movie
    # Gets all instances of tgt
    try:
        mRt = rt.loc[rt["Movie"]==tgt]
    except:
        return 0
    # Gets a count of all instances that got a rating of 5

    try:
        return mRt["Rating"].value_counts()[5] / len(mRt.index)
    except:
        return -1
    #Returns  (count of MovieRating == 5) / (total size of ratings dataset)

def probMovieGivenMovieRating(tgt, movie, rating):
    # P(Movie tgt | Movie == #)
    # int tgt:          Index of movie for which the prob is being calc'd
    # int movie:        Index of movie which the user has entered a rating for
    # int rating(1-5):  Rating the user has given the movie



    # Gets all instances of tgt
    try:
        mRt = rt.loc[rt["Movie"]==tgt]
    except:
        print("error getting tgt")

    # Isolates each unique user's id that has rated the tgt movie into a list
    uInd = mRt["User"].unique().tolist()
    print("done getting tgt")
    # Gets all ratings from users who gave a rating to tgt & movie
    mRt = rt.loc[uInd]
    uInd.sort()
    try:
        mRt = mRt.loc[rt["Movie"] == movie]
    except:
        print("error getting movie")
    print("done getting movie")
    uInd = mRt["User"].unique().tolist()
    mRt = rt.loc[uInd]
    print(uInd)
    print(mRt)




# Path to data files
DataPath = "Training/tRatings.csv"
MoviesPath = "moviesData.csv"
# Reads in ratings and converts it to a data frame
# Cols: User, Movie, Rating
rt = pd.DataFrame(pd.read_csv(DataPath))  # , index_col = "User"
rt.set_index("User",inplace=True, drop=False)

rtLength = len(rt.index)
# Cols: Index, Movie
mv = pd.DataFrame(pd.read_csv(MoviesPath))
mv.set_index('Index',inplace=True, drop=False)

mvLength = len(mv.index)
# print(mv)
# runMachine()


#print(probMovie(150))
probMovieGivenMovieRating(100, 250, 5)
#print(rt.columns.values)
# print(rt.loc[2])









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



    # Gets all instances of tgt being rated
    try:
        tRt = rt.loc[rt["Movie"]==tgt]
    except:
        print("error getting tgt")
    #print("done getting tgt")
    # Isolates each unique user's id that has rated the tgt into a list
    tInd = tRt["User"].unique().tolist()
    #tInd = pd.DataFrame(tInd)

    #tRt = rt.loc[tInd]
    tInd.sort()


    # Gets all instances of movie being rated
    try:
        mRt = rt.loc[rt["Movie"] == movie]
    except:
        print("error getting movie")
    #print("done getting movie")

    #print (mRt)
    # Isolates each unique user's id that has rated the movie into a list
    mInd = mRt["User"].unique().tolist()
    mInd.sort()

    #List of Users who've rated both tgt & movie
    gInd = []
    for t in tInd:
        for m in mInd:
            if(t == m):
                gInd.append(t)



    # Dataframe of all users & their ratings where they gave a rating to tgt & movie
    mRt = rt.loc[gInd]

    mvs = [tgt, movie]
    tmp = {"User":[], "Movie":[], "Rating":[]}
    mvsRatings = pd.DataFrame(tmp)

    for item in mvs:
        mvsRatings = mvsRatings.append(mRt.loc[mRt["Movie"] == item], ignore_index = True)


    mvsRatings = mvsRatings.astype('int32')
    mvsRatings.set_index("User", inplace=True, drop=False)
    # mvsRatings is a dataframe of tgt or movie ratings from user's who rated both

    if mvsRatings.empty:
        # If mvsRatings is empty then there are no user's that rated both so return 1 to not affect the probability equation
        return 1






#####################
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

for i in range(1, 3000):
    print(i)
    probMovieGivenMovieRating(i, 8, 5)
    probMovieGivenMovieRating(i, 45, 5)
    probMovieGivenMovieRating(i, 23, 5)
    probMovieGivenMovieRating(i, 115, 5)

#print(probMovie(150))
probMovieGivenMovieRating(45, 20, 5)
#print(rt.columns.values)
# print(rt.loc[2])








import tkinter as tk # PACKAGE USED FOR CREATING GUI
from tkinter import ttk
import pandas as pd

mvprd = "mvPredictor"
mvPredictor = __import__(mvprd)
from tkinter import * #IMPORTS ALL WIDGEST FROM THE PACKAGE

#import mvPred

app=tk.Tk()# CREATES THE WINDOW
app.geometry('900x500') # window size
app.title('Movie Predictor')
#print('hello world')
df1=pd.read_csv('moviesData.csv')
df1.set_index('Index',inplace=True, drop=False)
df2=df1["Movie"]
#<<<<<<< HEAD
#=======
#print (df1)
#>>>>>>> d5a554eb2b46e1a58fa429541cea0a9959a47da7

movies = []
for i in df2:# adds only the movies to a list
    movies.append(i)

mymovrat=[ ]#creates input list
predic_mov=[ ]#creates output list

labelTop = tk.Label(app,text = "Choose a movie") # CREATES A LABEL
labelTop.grid(column=0, row=0) #POSITION OF CREATED LABEL

combomov = ttk.Combobox(app,values=movies,state='readonly', width = 50) # CREATES A COMBO BOX. tHIS IS THE COMBOBOX THAT CONTAINED THE MOVIE NAME
combomov.grid(column=0, row=1) # POSITIONING OG COMBOBOX

comborat = ttk.Combobox(app,                             #CREATES A COMBOBOX THAT GIVES THE USER 5 OPTIONS TO INPUT THE RATING
                            values=[
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5"]
                        ,state='readonly')
comborat.grid(column=0, row=8) # PUTS THE RATING COMBOBOX ON THE APP WITH A POSYION

labelr = tk.Label(app, text = "Choose Rating")      # CREATES LABEL THAT TELLS USER TO CHOOSE A TRATING
labelr.grid(column=0, row=4)#  PUTS THE LABEL ON THE APP WITH A POSITION

def cmov(): # FUNCTION TO GIVE PROPERTY TO THE ADD RATING BUTTON. IT SELECTS THE MOVIE CHOSEN  AND THE RATINGS CHOSE. Gets the id and rating of the movie chosen
    entry.configure(state='normal')#enables text entry
    ind=combomov.current() +1
    #print(ind)
    mymovrat.append([ind, comborat.get()])# put the id and rating in a list
    entry.insert('2.0',combomov.get() +' Rating: '+ comborat.get() + ',\n')# IT DISPLAYS THE USERS CHOICES IN A jTextArea sorta component named entry
    entry.configure(state='disabled')#disables text entry

button = tk.Button(app, text='Add Rating', width=25, command = cmov)# add a putton and send its command to cmove,the function defined above
button.grid(column=0, row =15)# place button on the app woth postion

labelmo=tk.Label(app, text="Your Chosen Movies + Rating")
labelmo.grid(column =0 ,row =16)

entry=tk.Text(app,width = 45 ,height= 10 ,state='disabled')# creates a jtextArea sorta thing to display the movies chosen by the user
entry.grid(column =1, row =16)

pmovies =tk.Text(app,width = 45 ,height= 10,state='disabled')# creates a jtextArea sorta thing to display the movies that are predicted to the user. it should be placed  below the predict value button
pmovies.grid(column =0, row =24)

def pmov(): ##this is the function where the ML will essenatially perform. IT should choose the movie and the rating and this function is what the predict value buttton will do
    pmovies.configure(state='normal')
    usemov = pd.DataFrame(mymovrat, columns = ['user_mo_index', 'user_rat'])##puts the user chosen movie id and the user chosen rating in a df
    ratings = usemov.set_index("user_mo_index", drop=True)
    pmovies.insert('2.0',' Predicted movies with certainty:\n' )
    usemov = pd.DataFrame(mymovrat, columns = ['movieid', 'rating'])##puts the user chosen movie id and the user chosen rating in a df
    ratings = usemov.set_index("movieid", drop=True)
    predic_mov_id=mvPredictor.getPredictions(usemov)# sends df to getPrediction

    for x in predic_mov_id["movieID"]:#gets movie name from id
        predic_mov.append(df1.loc[x,"Movie"])


    #print(predic_mov)
    predic_mov_id['MovieName'] = predic_mov#adds movie name to output
    predic_mov_id = predic_mov_id.drop('movieID', 1)#removes id from output
    predic_mov_id = predic_mov_id[['MovieName','Certainty']]
    predic_mov_id.set_index('MovieName', inplace=True, drop=True)
    #print (predic_mov_id)
    pmovies.insert('2.0',predic_mov_id )#display output
    ####disables buttons####
    button.configure(state='disabled')
    button1.configure(state='disabled')
    pmovies.configure(state='disabled')
    

button1 = tk.Button(app, text='Predict Film', width=25, command=pmov)# this is the predict values button that does should dispaly the predicted  moivies to the user
button1.grid(column=0, row =22)

app.mainloop() # runs the app as a loop . it is important for app to run in tkinters a loop . it is important for app to run in tkinter
import tkinter as tk # PACKAGE USED FOR CREATING GUI
from tkinter import ttk
import pandas as pd


from tkinter import * #IMPORTS ALL WIDGETS FROM THE PACKAGE



app=tk.Tk()# CREATES THE WINDOW
app.geometry('900x900') # DEFAULT WINDOW SIZE WHEN IT OPENS

df1=pd.read_csv('moviesData.csv')
df2=df1[["Movie"]]
movies = [ ]
for i in df2.iterrows():
    movies.append(i)

labelTop = tk.Label(app,text = "Choose your favourite movie") # CREATES A LABEL
labelTop.grid(column=0, row=0) #POSITION OF CREATED LABEL

combomov = ttk.Combobox(app,                               # CREATES A COMBO BOX. tHIS IS THE COMBOBOX THAT CONTAINED THE MOVIE NAME
                            values=movies)#### contains all the movies, will edit the way it looks later
print(dict(combomov))
combomov.grid(column=0, row=1) # POSITIONING OG COMBOBOX
#comboExample.current(1)

comborat = ttk.Combobox(app,                             #CREATES A COMBOBOX THAT GIVES THE USER 5 OPTIONS TO INPUT THE RATING
                            values=[
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5"]
                        )
labelr = tk.Label(app, text = "Choose Rating")      # CREATES LABEL THAT TELLS USER TO CHOOSE A TRATING
labelr.grid(column=0, row=4)#  PUTS THE LABEL ON THE APP WITH A POSITION

comborat.grid(column=0, row=8) # PUTS THE RATING COMBOBOX ON THE APP WITH A POSYION

def cmov(): # FUNCTION TO GIVE PROPERTY TO TTHE ADD RATING BUTTON. IT SELECTS THE MOVIE CHOSEN  AND THE RATINGS CHOSE. pUSTS THOSE VALUES IN USERMOV AND USER RAT.
    entry.insert('2.0',combomov.get() +' '+ comborat.get()) # IT DISPLAYS THE USERS CHOICES IN A jTextArea sorta component named entry
    usermov = combomov.get()# get selected movie
    userat = int(comborat.get())# get selected rating

app.title('Movie Predictor')
button = tk.Button(app, text='Add Rating', width=25, command = cmov)# add a putton and send its command to cmove,the function defined above

button.grid(column=0, row =15)# place button on the app woth postion
#button.pack()
labelmo=tk.Label(app, text="Your Chosen Movies + Rating")

labelmo.grid(column =0 ,row =16)

entry=tk.Text(app)# creates a jtextArea sorta thing to display the movies chosen by the user
entry.grid(column =1, row =16) # should be placed to the right and below the add rating button

pmovies =tk.Text(app)# creates a jtextArea sorta thing to display the movies that are predicted to the user. it should be placed  below the predict value button
pmovies.grid(column =0, row =23)

def pmov(): ####### this is the function where the ML will essentially perform. IT should choose the movie and the rating and this function is what the predict value buttton will do
    pmovies.insert('2.0','the predicted movies are' )

button1 = tk.Button(app, text='Predict Film', width=25, command=pmov)# this is the predict values button that does should dispaly the predicted  moivies to the user
button1.grid(column=0, row =22)

#entry.pack()
#print(comboExample.current(), comboExample.get())

app.mainloop() # runs the app as a loop . it is important for app to run in tkinter
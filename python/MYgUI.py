import tkinter as tk
from tkinter import ttk
from tkinter import *

app=tk.Tk()#where m is the name of the main window object
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite movie")
labelTop.grid(column=0, row=0)

combomov = ttk.Combobox(app,
                            values=[
                                    "Movie 1",
                                    "Movie 2",
                                    "Movie 3",
                                    "Movie 4",
                                    "Movie 5",
                            ])
print(dict(combomov))
combomov.grid(column=0, row=1)
#comboExample.current(1)

comborat = ttk.Combobox(app,
                            values=[
                                    "1",
                                    "2",
                                    "3",
                                    "4",
                                    "5"]
                        )
labelr = tk.Label(app,
                    text = "Choose Rating")
labelr.grid(column=0, row=4)

comborat.grid(column=0, row=8)





#entry.pack()


#print(comboExample.current(), comboExample.get())

app.mainloop()
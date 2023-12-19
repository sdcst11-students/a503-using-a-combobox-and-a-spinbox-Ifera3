"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *

def yer():
    l = []
    for i in range(1980,2024):
        l.append(i)
    return l

global dayd
dayd = []#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,27,28,29,30,31]

window = tk.Tk()
window.title('Info')

spinY = ttk.Combobox(window, values=yer())
spinY.set(2000)
spinM = ttk.Combobox(window, values=['January','Febuary','March','April','May','June','Jully','Augest','September','October','November','December'])
spinM.set('January')

def day():
    dayd.clear()
    if spinM.get() == 'Febuary':
        d = 28
    else:
        d = 32
    for i in range(d):
        dayd.append(i)

spinD = ttk.Combobox(window, values=dayd, postcommand=day())
spinD.set(1)
b = Button(window)
e = Entry(window)

def go(event):
    print(event)
    r = f"{spinM.get()} {spinD.get()}, {spinY.get()}" 
    e.delete(0,END)
    e.insert(0,r)

b.bind('<Button>', go)
#window.bind('<Button-1>', day)

spinM.grid(row=1, column=1)
spinD.grid(row=1, column=2)
spinY.grid(row=1, column=3)
b.grid(row=1, column=4)
e.grid(row=1, column=5)

window.mainloop()

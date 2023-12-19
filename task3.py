#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title('tk')

l1 = Label(window, text='Pricable')
l2 = Label(window, text='Rate in decamle')
l3 = Label(window, text='compunds per year')
l4 = Label(window, text='Term in years')
l5 = Label(window, text='Acumulated Money')
ep = Entry(window)
er = Entry(window)
en = Entry(window)
et = Entry(window)
b = Button(window, text='=')
ea = Entry(window)

def a(event):
    print(event)
    ea.delete(0,END)
    try:
        A = (int(ep.get()) * (1 + float(er.get())/int(en.get()))**(int(en.get())*int(et.get())))
        ea.insert(0,f'${round(A,2)}')
    except:
        ea.insert(0,'Fail')

b.bind('<Button>', a)

l1.grid(row=1,column=1)
l2.grid(row=1,column=2)
l3.grid(row=1,column=3)
l4.grid(row=1,column=4)
l5.grid(row=1,column=6)
ep.grid(row=2,column=1)
er.grid(row=2,column=2)
en.grid(row=2,column=3)
et.grid(row=2,column=4)
b.grid(row=2,column=5)
ea.grid(row=2,column=6)

window.mainloop()
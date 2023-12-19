#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title('Calculater')

entery1 = Entry(window)
spin = ttk.Spinbox(window,values=['+','-','x','/','^'],width=3)
spin.set('+')
entery2 = Entry(window)
button1 = Button(window,text='=', border=1)
entery3 = Entry(window)

def calculate(event):
    print(event)
    entery3.delete(0,END)
    try:
        if spin.get() == '+':
            entery3.insert(0, int(entery1.get()) + int(entery2.get()))
        elif spin.get() == '-':
            entery3.insert(0, int(entery1.get()) - int(entery2.get()))
        elif spin.get() == 'x':
            entery3.insert(0, int(entery1.get()) * int(entery2.get()))
        elif spin.get() == '/':
            entery3.insert(0, int(entery1.get()) / int(entery2.get()))
        elif spin.get() == '^':
            entery3.insert(0, int(entery1.get()) ** int(entery2.get()))
    except:
        entery3.insert(0,'failed')

button1.bind('<Button>', calculate)

entery1.grid(row=1, column=1, padx= 2)
spin.grid(row=1, column=2, padx= 2)
entery2.grid(row=1, column=3, padx= 2)
button1.grid(row=1, column=4, padx= 2)
entery3.grid(row=1, column=5, padx= 2)

window.mainloop()
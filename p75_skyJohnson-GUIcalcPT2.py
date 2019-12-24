# p75_skyJohnson-GUIcalcPT2.py
# Sky Johnson
# 4/30/14
# Python 3.3.3
# Description: Program to create a calculator using a GUI

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.title("Calculator")
window.geometry("320x453")
e = tkinter.Entry(window, width = 40)
e.grid(row = 0, column = 0, columnspan = 4)

def myFunction(n):
    incr = 0
    for i in range(0,40):
        incr += 1
    s = e.get()
    e.insert(incr,n)
    if n == '=':
        splitString = s.split('=')
        e.insert(incr,eval(splitString[0]))
    if n == 'Clear':
        e.delete(0,tkinter.END)
        

w = []
w.append(tkinter.Button(window,
                        text = "1",
                        width = 10, height = 5,
                        command = lambda n = 1: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "2",
                        width = 10, height = 5,
                        command = lambda n = 2: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "3",
                        width = 10, height = 5,
                        command = lambda n = 3: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "+",
                        width = 10, height = 5,
                        command = lambda n = '+': myFunction(n)))
w.append(tkinter.Button(window,
                        text = "4",
                        width = 10, height = 5,
                        command = lambda n = 4: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "5",
                        width = 10, height = 5,
                        command = lambda n = 5: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "6",
                        width = 10, height = 5,
                        command = lambda n = 6: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "-",
                        width = 10, height = 5,
                        command = lambda n = '-': myFunction(n)))
w.append(tkinter.Button(window,
                        text = "7",
                        width = 10, height = 5,
                        command = lambda n = 7: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "8",
                        width = 10, height = 5,
                        command = lambda n = 8: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "9",
                        width = 10, height = 5,
                        command = lambda n = 9: myFunction(n)))
w.append(tkinter.Button(window,
                        text = "=",
                        width = 10, height = 11,
                        command = lambda n = '=': myFunction(n)))
w.append(tkinter.Button(window,
                        text = "0",
                        width = 21, height = 5,
                        command = lambda n = 0: myFunction(n)))
w.append(tkinter.Button(window,
                        text = ".",
                        width = 10, height = 5,
                        command = lambda n = '.': myFunction(n)))
w.append(tkinter.Button(window,
                        text = "Clear",
                        width = 45, height = 5,
                        command = lambda n = 'Clear': myFunction(n)))

w[0].grid(row = 1, column = 0)
w[1].grid(row = 1, column = 1)
w[2].grid(row = 1, column = 2)
w[3].grid(row = 1, column = 3)
w[4].grid(row = 2, column = 0)
w[5].grid(row = 2, column = 1)
w[6].grid(row = 2, column = 2)
w[7].grid(row = 2, column = 3)
w[8].grid(row = 3, column = 0)
w[9].grid(row = 3, column = 1)
w[10].grid(row = 3, column = 2)
w[11].grid(row = 3, rowspan = 2, column = 3)
w[12].grid(row = 4, column = 0, columnspan = 2)
w[13].grid(row = 4, column = 2)
w[14].grid(row = 5, column = 0, columnspan = 4)

window.mainloop()

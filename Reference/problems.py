import sys
import tkinter

from tkinter import ttk
from problems_DB import problems_set


if len(sys.argv) != 2:
    print("Please Input a Parameter: p / t")
    sys.exit()

if parameter == 'p':

    window = tkinter.Tk()
    window.title("Main")
    window.geometry('1080x600')
    window.resizable(False, False)

    def buttonClicked():
        labelNew.configure(text='Problem Number: ' + name.get())
        description.configure(text='Title: ' + problems_set[name.get()][0])
        topic.configure(text='Topic: ' + problems_set[name.get()][1])
        link.configure(text='Link: ' + problems_set[name.get()][2])
        source.configure(text='Source: ' + problems_set[name.get()][3])
        difficulty.configure(text='Difficulty: ' + problems_set[name.get()][4])

    label = ttk.Label(window, text = "Input the problem no. (ex. H12345)")
    label.grid(column=0, row=0)

    button = ttk.Button(window, text="click", command=buttonClicked)
    button.grid(column=1, row=2)

    name = tkinter.StringVar()
    textbox = ttk.Entry(window, width=24, textvariable=name)
    textbox.grid(column=0, row=2)

    labelNew = ttk.Label(window, text="")
    labelNew.grid(column=0, row=3)
    
    space = ttk.Label(window, text="")
    space.grid(column=0, row=4)

    description = ttk.Label(window, text="")
    description.grid(column=0, row=5)

    topic = ttk.Label(window, text="")
    topic.grid(column=0, row=6)

    link = ttk.Label(window, text="")
    link.grid(column=0, row=7)

    source = ttk.Label(window, text="")
    source.grid(column=0, row=8)

    difficulty = ttk.Label(window, text="")
    difficulty.grid(column=0, row=9)

    window.mainloop()

elif parameter == 't':

    window = tkinter.Tk()
    window.title("Main")
    window.geometry('500x350')
    window.resizable(False, False)



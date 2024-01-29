from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S Uhr")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    root.after(1000, update)

root = Tk()
root.title("Uhr")
root.iconbitmap(r"D:\Dev\python programme\clock\time-1606153.ico")

time_label = Label(root, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(root, font=("Ink Free", 25))
day_label.pack()

date_label = Label(root, font=("Ink Free", 30))
date_label.pack()

update()

root.mainloop()
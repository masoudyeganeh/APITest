from tkinter import *
import os

root = Tk()
# path = 'C:\Folder Name'
path = 'C:/Users/m.yeganeh/PycharmProjects/APITest/out.xlsx'

def open():
    os.startfile(path, 'open')

button = Button(root, text="Open File Direction or File", command=open)
button.pack()

root.mainloop()
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import pandas as pd
import applicationConfig as appconf
import os

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*csv')])
    if file_path is not None:
        appconf.path = file_path


def uploadFiles():
    pb1 = Progressbar(
        ws,
        orient=HORIZONTAL,
        length=300,
        mode='determinate'
    )
    pb1.grid(row=4, columnspan=4, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    import main
    main.customerOrdersObjectList
    main.customerOrdersCompareKeysTestResult
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=5, columnspan=3, pady=10)

def open():
    path = 'C:/Users/m.yeganeh/PycharmProjects/APITest/out.xlsx'
    os.startfile(path, 'open')

adhar = Label(
    ws,
    text='سناریو تست را انتخاب کنید:  '
)
adhar.grid(row=0, columnspan=1, padx=10)

adharbtn = Button(
    ws,
    text='انتخاب',
    command=lambda: open_file()
)
adharbtn.grid(row=0, column=1)

upld = Button(
    ws,
    text='تست',
    command=uploadFiles
)
upld.grid(row=1, column=1, pady=10)

openbtn = Button(ws, text="مشاهده نتیجه تست", command=open)
openbtn.grid(row=3, column=1, pady=10)

ws.mainloop()

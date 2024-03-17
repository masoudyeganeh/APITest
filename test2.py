import json
import generalMethods

# f = open('port_man_contract_14020929_1051841')
#
# data = json.load(f)
#
# c = generalMethods.count_keys(data)
#
# print(len(list(c)))
# # all_keys_list = list(dict.fromkeys(list(get_keys(data))))
# #
# # print(all_keys_list)
#
# f.close()


import tkinter as tk
from tkinter import filedialog

def on_submit():
    pass

app = tk.Tk()
app.title("تست اتومات سرویس")
app.geometry("400x300")

label = tk.Label(app, text="Enter your name:")
label.pack()

entry = tk.Entry(app)
entry.pack()

submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack()

app.mainloop()

def getLocalFile():
    root=tk.Tk()
    root.withdraw()

    filePath=filedialog.askopenfilename()

    print('File path：',filePath)
    return filePath

if __name__ == '__main__':
    getLocalFile()
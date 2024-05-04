import tkinter as tk
#from tkinter import ttk
import  ttkbootstrap as ttk


def convert():
    print("convert time")
    m = entryInt.get()
    print(f"m={m}")
    k = m * 1.609344
    print(f"k={k}")
    outputString.set(f"{k:.3f}")


#window 
window = ttk.Window(
    themename = 'journal'
)
window.title("demo")
window.geometry('640x480')

#title
title_label = ttk.Label(
    master=window,
    text = "Miles to Kilometers",
    font = "Calibri 24 bold"
)
title_label.pack()

input_frame = ttk.Frame(    master = window )

entryInt = tk.IntVar()
entry = ttk.Entry( master=input_frame, textvariable = entryInt)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
outputString = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text='output',
    font = "Calibri 24",
    textvariable=outputString  
).pack(pady=10)

#run
window.mainloop()

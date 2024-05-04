import tkinter as tk
#from ttkbootstrap import ttk
from tkinter import ttk

def btnClicked():
    label['text'] = entry.get()
    entry['state'] = 'disabled'

def btn2Clicked():
    label['text'] = 'some text'
    entry['state'] = 'enabled'


window = tk.Tk()
window.title('getting and setting widgets')

label = ttk.Label(
    master=window,
    text = 'my label'
)
label.pack()

entry = ttk.Entry( master=window )
entry.pack()

button = ttk.Button(
    master=window,
    text='my button',
    command=btnClicked
)
button.pack()

btn2 = ttk.Button(
    master=window,
    text='enable button',
    command=btn2Clicked
)
btn2.pack()


window.mainloop()
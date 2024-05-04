import tkinter as tk
from ttkbootstrap import ttk
#from tkinter import ttk

def btnFunct(entry_string):
    print('a button was pressed')
    print(entry_string.get())

def outer_funct(parameter):
    def inner_funct():
        print('a button was pressed')
        print(parameter.get())    
    return inner_funct    

#setup
window = tk.Tk()
window.title('buttons, function and arguments')
window.geometry('600x400')

#widgets
entryStr = tk.StringVar(value='test')
entry = ttk.Entry(
    master=window,
    textvariable=entryStr,
)
entry.pack()

button = ttk.Button(
    master=window,
    text="button",
    command=lambda: btnFunct(entryStr)
)
button.pack()


button2 = ttk.Button(
    master=window,
    text="button2",
    command= outer_funct(entryStr)
)
button2.pack()


#run
window.mainloop()
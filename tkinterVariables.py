import tkinter as tk
#from ttkbootstrap import ttk
from tkinter import ttk

def btnFunction():
    print(strVar.get())
    strVar.set("button pressed")


window = tk.Tk()
window.title('Tkinter Variables')

#tkinter variable

strVar = tk.StringVar( value='Start Value')
myStrVar = tk.StringVar( value='test')

#widgets
label = ttk.Label(
    master=window,
    text = "the label",
    textvariable=strVar
    
)
label.pack(padx=5,pady=5)

entry = ttk.Entry(
    master=window,
    textvariable=strVar
)
entry.pack(padx=5,pady=5)

btn = ttk.Button(
    master=window,
    text="button",
    command=btnFunction
)
btn.pack()

entry1 = ttk.Entry(
    master=window,
    textvariable=myStrVar
)
entry1.pack(padx=5,pady=5)

entry2 = ttk.Entry(
    master=window,
    textvariable=myStrVar
)
entry2.pack(padx=5,pady=5)

label1 = ttk.Label(
    master=window,
    textvariable=myStrVar
    
)
label1.pack(padx=5,pady=5)

window.mainloop()
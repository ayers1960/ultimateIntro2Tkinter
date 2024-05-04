import tkinter as tk
from tkinter import ttk


def bntHelloClicked():
    print("hello")

def  button_function():
    print("a button was pressed")

window = tk.Tk()
window.title("Window and Widgets")
#window.geometry("800x500")

#create widgets

## ttk widgets
label = ttk.Label(
    master=window,
    text='This is a test'
)
label.pack()

text = tk.Text(
    master=window,
)
text.pack(pady=(10,25))

entry = ttk.Entry(master=window)
entry.pack()

myLabel = ttk.Label(
    master=window,
    text="my label"
)
myLabel.pack()

button = ttk.Button(
    master=window,
    text='A Button',
    command=button_function
)
button.pack(pady=25)

btnHello = ttk.Button(
    master=window,
    text='Print Hello',
    #command=bntHelloClicked
    command=lambda: print('Hello')
)
btnHello.pack()
#run
window.mainloop()
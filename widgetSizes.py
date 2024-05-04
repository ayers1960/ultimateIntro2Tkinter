import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x300')
window.title('Place')

#widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'green')
label2 = ttk.Label(
    window, 
    text = 'Label 2', 
    background = 'red',
    width=50
)

"""
# pack
label1.pack()
label2.pack( fill='x')
"""

#grid
window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure((0,1), weight=1, uniform='a')

label1.grid(row=0,column=0)
label2.grid(row=1,column=0, sticky="nsew")

#run
window.attributes("-topmost",True)
window.mainloop()
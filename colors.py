import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from random import randint, choice
from datetime import datetime
import pprint



#window
window = tk.Tk()
window.geometry('400x300')
window.title('Colors')

ttk.Label(window, background = "#321654").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#654321").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#123456").pack(expand = True,fill = 'both')

ttk.Label(window, background = "#842").pack(expand = True,fill = 'both')

ttk.Label(window, background = "#000").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#FFF").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#111").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#333").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#555").pack(expand = True,fill = 'both')
ttk.Label(window, background = "#777").pack(expand = True,fill = 'both')

window.attributes("-topmost",True)
window.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import randint, choice
from datetime import datetime
import pprint

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('300x400')
        self.title('Extra Windows')    
        self.attributes("-topmost",True)

        self.L1 = ttk.Label(self, text='A Label').pack()
        self.B1 = ttk.Button(self, text='Close Button', command=self.destroy).pack()    
        self.L2 = ttk.Label(self, text='A Label').pack(expand=True)


def ask_yes_no():
    """ good messagebox documentation @ doc.python.org """
    answer = messagebox.askquestion("title", "body")
    #answer = messagebox.showinfo('info title', 'some information')
    #answer = messagebox.showerror('error title', 'some information')    
    print(answer)

def create_window():
    global extraWindow
    extraWindow = Extra()

def close_window():
    extraWindow.destroy()

#window
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple Windows')

button1 = ttk.Button(
    window, 
    text = 'open main window',
    command= create_window)
button1.pack(expand = True)

button2 = ttk.Button(
    window, 
    text = 'close main window',
    command = close_window)

button2.pack(expand = True)

button3 = ttk.Button(
    window, 
    text = 'create yes/no window',
    command = ask_yes_no
)
button3.pack(expand = True)


window.attributes("-topmost",True)
window.mainloop()

import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from random import randint, choice
from datetime import datetime
import pprint



#window
window = tk.Tk()
window.geometry('400x300')
window.title('Styling')

#print (font.families())

#style
style = ttk.Style()
#print(style.theme_names())
#style.theme_use('classic')

#style.configure(
#    'TButton', 
#    foreground='green',
#    font = ('Noto Serif',10),    
#    )


newTButton = 'new.TButton'   
style.configure(
    newTButton, 
    foreground='green',
    font = ('Noto Serif',20),    
    )
style.map(
    newTButton,
    foreground = [
        ('pressed', 'red'),
        ('disabled', 'yellow'),
    ],
    background = [
        ('pressed', 'green'), 
        ('active', 'blue'),
    ],
    font = [
        ('pressed', ('Noto Serif',10))
    ]
)
style.configure('TFrame', background='pink' )

#widgets
label = ttk.Label(
    window, 
    text = """A Label\nAnd then type on anther line""",
    background='red',
    foreground='white',
    font = ('Noto Serif',20),
    justify = 'center'
)
label.pack()

button = ttk.Button(
    window, 
    text = 'A Button',
    style=newTButton,
    #state='disabled'
)
button.pack()

frame = ttk.Frame(window, height= 100, width=100)
frame.pack()



window.attributes("-topmost",True)
window.mainloop()

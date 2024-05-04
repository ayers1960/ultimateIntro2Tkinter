import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x400')
window.title('Stacking Widgets')

#widgets
label1 = ttk.Label(window, text='label 1', background = 'green')
label2 = ttk.Label(window, text='label 2', background = 'red' )
label3 = ttk.Label(window, text='Label 3', background = 'blue')
#label2.lower()
#label1.lift()

button1 = ttk.Button(window, text = 'raise label 1', command=lambda: label1.tkraise())
button2 = ttk.Button(window, text = 'raise label 2', command=lambda: label2.tkraise(aboveThis=label1))
button3 = ttk.Button(window, text = 'raise label 3', command=lambda: label3.tkraise())


#layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=50, y=100, width=140, height=100)

button1.place(rely=1, relx=0.8, anchor = 'se')
button2.place(rely=1, relx=1, anchor = 'se')
button3.place(rely=1, relx=0, anchor = 'sw')

#run
window.attributes("-topmost",True)
window.mainloop()
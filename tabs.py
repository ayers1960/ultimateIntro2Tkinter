import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('640x480')
window.title('Tab Widget')

#notebook / tab widget
notebook =  ttk.Notebook(
    master = window
)
notebook.pack()

tab1 = ttk.Frame(
    master = notebook
)

label1=ttk.Label(
    master=tab1,
    text='text in tab1'
)
label1.pack()
button1 = ttk.Button(
    master=tab1,
    text='tab1-button'
)
button1.pack()

tab2 = ttk.Frame(
    master=notebook
)
label2=ttk.Label(
    master=tab2,
    text='text in tab2'
)
label2.pack()
button2 = ttk.Button(
    master=tab2,
    text='tab2-button'
)
button2.pack()
entry2=ttk.Entry(tab2)
entry2.pack()


tab3 = ttk.Frame(
    master=notebook
)
label3=ttk.Label(
    master=tab3,
    text='text in tab3'
)
label3.pack()
button3a = ttk.Button(
    master=tab3,
    text='tab3a-button'
)
button3a.pack()

button3b = ttk.Button(
    master=tab3,
    text='tab3b-button'
)
button3b.pack()
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.pack()

#run
window.mainloop()
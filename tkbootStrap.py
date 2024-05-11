import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

#window
window = ttk.Window( themename = 'darkly')
window.title('ttk bootstrap intro')
window.geometry('400x300')


label = ttk.Label(window, text = 'Label')
label.pack()

button1 = ttk.Button(window, text = 'Red', bootstyle=ttk.DANGER)
button1.pack(pady=10)

button2 = ttk.Button(window, text = 'Warning', bootstyle=(ttk.WARNING, ttk.OUTLINE))
button2.pack(pady=10)

button3 = ttk.Button(window, text = 'Green', bootstyle=ttk.SUCCESS)
button3.pack(pady=10)

#run
window.mainloop()
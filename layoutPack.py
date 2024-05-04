import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x600')
window.title('Layout Intro')

#widgets
label1 = ttk.Label(window,text='Label 1', background='red')
label2 = ttk.Label(window,text='Label 2', background='blue')
label3 = ttk.Label(window,text='last of the labels', background='green')
button = ttk.Button(window, text='Button')


#layout
label1.pack(side='top',fill='both', expand=True, padx=10, pady=10)
label2.pack(side='left',fill='both', expand=True)
label3.pack(side='top',expand=True, fill='both' )
button.pack(side='top',expand=True, fill='both')


"""
#grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=3)

label1.grid(row=0, column=1, sticky='NSEW')
#label2.grid(row=0, column=0, sticky = 'nsew')
label2.grid(row=1, column=1, sticky = 'nsew',columnspan=2)
"""

"""
#place   top left is 0,0
label1.place(x=100,y=100, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=0.50, anchor='center')
"""

#run
window.mainloop()
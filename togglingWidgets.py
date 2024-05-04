import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Toggling Widgets')

"""
# place
def toggle_label_place():
    global labelVisible
    if labelVisible:
        label.place_forget()
        labelVisible = False
    else:
        labelVisible = True
        label.place(relx=0.5, rely=0.5, anchor='center')

button = ttk.Button(window, text='toggle label', command = toggle_label_place)
button.place(x=10,y=10)
labelVisible = True
label = ttk.Label(window, text='A Label')
label.place(relx=0.5, rely=0.5, anchor='center')
"""

"""
#grid
def toggle_label_grid():
    global labelVisible
    if labelVisible:
        label.grid_forget()
        labelVisible = False
    else:
        labelVisible = True
        label.grid(column=1, row=0)


window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
button = ttk.Button(window, text='toggle label', command = toggle_label_grid)
button.grid(column=0, row=0)
labelVisible = True
label = ttk.Label(window, text='A Label')
label.grid(column=1, row=0)
"""

#pack
def toggle_label_pack():
    global labelVisible
    if labelVisible:
        label.pack_forget()
        frame.pack(expand=True, before=button)
        frame.config()
        labelVisible = False
    else:
        labelVisible = True
        label.pack(expand=True, before=button)
        frame.pack_forget()

window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
button = ttk.Button(window, text='toggle label', command = toggle_label_pack)
labelVisible = True

frame = ttk.Frame(window)

label = ttk.Label(window, text='A Label')
label.pack(expand=True)
button.pack()
frame = ttk.Frame(window)


#run
window.attributes("-topmost",True)
window.mainloop()
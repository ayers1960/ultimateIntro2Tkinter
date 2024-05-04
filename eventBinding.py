import tkinter as tk
#from ttkbootstrap import ttk
from tkinter import ttk

"""
http://pythontutorial.net/tkinter/tkinter-event-binding
"""


def get_pos(event):
    print(f"x{event.x}: y: {event.y}")

#setup
window = tk.Tk()
window.title('event binding')
window.geometry('600x400')


#widgets
text = tk.Text(
    master=window,
    width=25,
    height=5,
)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(
    master=window,
    text='clickme'
)
btn.pack()

# events
btn.bind("<Alt-KeyPress-a>", lambda event: print(event))
#text.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda event: print(event.char))
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))

text.bind('<FocusIn>', lambda event: print('text has the focus'))
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))
text.bind('<FocusOut>', lambda event: print('text has LOST the focus'))
#run
window.mainloop()
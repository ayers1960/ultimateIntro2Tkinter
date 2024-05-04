import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
#window.geometry("640x480")
window.title("Frames and Parenting")

#frame
frame = ttk.Frame( 
    master=window, 
    width=200,
    height=200,
    borderwidth=10,
    relief=tk.GROOVE,
)
frame.pack_propagate(False)
frame.pack(side='left')
# master setting
label = ttk.Label(
    master=frame,
    text="Label in frame"
)
label.pack()

button = ttk.Button(
    master=frame,
    text='button in  a frame'
)
button.pack()

#example
label2 = ttk.Label(window, text='label outside frame')
label2.pack(side='left')


myFrame = ttk.Frame(
    master=window
)
myFrame.pack(side='right')

myLabel = ttk.Label(
    master=myFrame,
    text = 'my Label',
)
myLabel.pack()
myButton = ttk.Button(
    master=myFrame,
    text='my button',
)
myButton.pack()

myEntry = ttk.Entry(
    master=myFrame
)
myEntry.pack()


#run 
window.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from random import choice

#window
window = tk.Tk()
#window.geometry("640x480")
window.title("Sliders")

toVar = 25
#slider 
scaleVal = tk.DoubleVar(value=12.5)
scale = ttk.Scale(
    master=window,
    command = lambda value: progress.stop(),
    from_ =0,
    to = toVar,
    length=300,
    orient = 'horizontal',
    variable = scaleVal
)
scale.pack()


#progress
progress = ttk.Progressbar(
    master=window,
    variable = scaleVal,
    maximum=toVar,
    orient = 'horizontal',
    mode = 'indeterminate',
    length= 400,
)
progress.pack()
#progress.start(1000)

#Scrolledtext
scrolledText = scrolledtext.ScrolledText(
    master = window,
    width = 100,
    height = 8,
)
scrolledText.pack()

#exercise


MyScaleVal = tk.DoubleVar()
myScale = ttk.Scale(
    master=window,
    command = lambda value: progress.stop(),
    from_ =0,
    to = toVar,
    length=300,
    orient = 'horizontal',
    variable = MyScaleVal
)
myScale.pack()


#progress
myProgress = ttk.Progressbar(
    master=window,
    variable = MyScaleVal,
    maximum=toVar,
    orient = 'vertical',
)
myProgress.pack()

MyLabel = ttk.Label(
    master=window,
    textvariable=MyScaleVal
)
MyLabel.pack()

myProgress.start()



#run
window.mainloop()
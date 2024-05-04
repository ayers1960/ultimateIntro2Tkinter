import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x600')
window.title('Layout Intro')


#top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame,text='First Label', background='red')
label2 = ttk.Label(top_frame,text='Label 2', background='blue')

#middle widget
label3 = ttk.Label(window,text='Another label', background='green')

#bottom frame

bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame,text='last of the labels', background='orange')
button = ttk.Button(bottom_frame, text='A Button')
button2 = ttk.Button(bottom_frame, text='AnotherButton')


btmRightFrame = ttk.Frame(bottom_frame)
button3 = ttk.Button(btmRightFrame, text='Button 3')
button4 = ttk.Button(btmRightFrame, text='Button 4')
button5 = ttk.Button(btmRightFrame, text='Button 5')


#top layout
label1.pack(    side='left', fill='both', expand=True)
label2.pack(    side='left', fill='both', expand=True)
top_frame.pack( side='top', fill='both', expand=True)

#middle widget: label3
label3.pack(expand=True)


#bottom layout

button.pack( side='left' ,expand=True, fill='both',)
label4.pack( side='left' ,expand=True, fill='both')
button2.pack(side='left' ,expand=True, fill='both')


button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')

btmRightFrame.pack(expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both')
#run
window.attributes("-topmost",True)
window.mainloop()
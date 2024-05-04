import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('400x800')
window.title('Place')

#widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
label4 = ttk.Label(window, text = 'Label 4', background = 'yellow')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')
entry = ttk.Entry(window)


#layout
label1.place( x=300, y=200, width=300, height=50 )
label2.place(relx=0.0, rely=0.0, relwidth=0.4, relheight=0.5)
label3.place(x=0, y=0, width=160, height=400)

button1.place(relx=1,rely=1, anchor='se')


#frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='Frame Label', background='yellow')
frame_button = ttk.Button(frame, text='Frame Button')

#frame Layout
frame.place(relx = 0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

exerLabel = ttk.Label(
    window,
    text='exerLabel', 
    background='purple', 
    foreground='white',
    anchor='center'
)
exerLabel.place(relx=0.5, rely=0.5, relwidth=0.50,  height=200, anchor='center' )


#run
window.attributes("-topmost",True)
window.mainloop()
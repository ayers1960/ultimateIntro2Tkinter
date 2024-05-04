import tkinter as tk
from ttkbootstrap import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

items = ('ice cream', 'pizza', 'broccoli')
foodStr = tk.StringVar(value=items[0])
combo = ttk.Combobox(
    master=window,
)
combo.configure(values=items, textvariable=foodStr)
combo.pack()

#events
combo.bind("<<ComboboxSelected>>", 
            lambda event: combo_label.config(text=f"selected: {foodStr.get()}"))

combo_label = ttk.Label(window, text="pick a food")
combo_label.pack()


#Spinbox
spinInt = tk.IntVar(value=12)
spin = ttk.Spinbox(
    master=window,
    from_ =3,
    to = 21,
    increment = 3,
    command = lambda: print(spinInt.get()),
    textvariable=spinInt,
)
spin.pack()
spin.bind("<<Decrement>>", lambda event: print('down'))
spin.bind("<<Increment>>", lambda event: print('Up'))


#Spinbox
letters = ('A','B','C','D','E')

spinStr = tk.StringVar(value=letters[0])
spin2 = ttk.Spinbox(
    master=window,
    textvariable=spinStr,
    values=letters,
)
spin2.pack()
spin2.bind("<<Decrement>>", lambda event: print(spinStr.get()))

#run
window.mainloop()
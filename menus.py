import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Menus")


#menu
menu = tk.Menu(   master=window)

#sub menu
fileMenu = tk.Menu(
    master=menu,
    tearoff=False,
)
fileMenu.add_command(label = 'New', command = lambda: print('New File'))
fileMenu.add_command(label = 'Open', command = lambda: print('Open File'))
fileMenu.add_separator()
menu.add_cascade(
    label='File',
    menu = fileMenu
)

#another sub menu
helpMenu = tk.Menu(
    master=menu,
    tearoff = False
)
menu.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label = 'Help', command = lambda: print(helpMenuStr.get()))
helpMenuStr = tk.StringVar()
helpMenu.add_checkbutton(
    label='check', 
    onvalue='on',
    offvalue='off',
    variable = helpMenuStr

)

myMenu = tk.Menu(menu,tearoff= False)
myMenu.add_command(label='test1')
window.configure(menu = menu)
menu.add_cascade(label='myMenu', menu=myMenu)

mySubMenu = tk.Menu(menu,tearoff=False)



myMenu.add_cascade(
    label='sub menu', 
    menu= mySubMenu
)
mySubMenu.add_cascade(
    label='sub sub menu', 
  
)

#menu button

menuButton = ttk.Menubutton(
    master=window,
    text='Menu Button'
)
menuButton.pack()
btnSubMenu = tk.Menu(menuButton, tearoff=False)

menuButton.configure(menu=btnSubMenu)
btnSubMenu.add_command(label = 'New', command = lambda: print('New File'))


window.mainloop()
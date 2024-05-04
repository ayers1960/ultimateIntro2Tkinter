import tkinter as tk
from ttkbootstrap import ttk
#from tkinter import ttk


#setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button
btnStr = tk.StringVar(value='button with StringVar')
def button_func():
    print("a basic button")
    print (radioVar.get() )


button = ttk.Button(
    master=window,
    text='a simple button',
    command=button_func,
    textvariable=btnStr
)
button.pack()

#checkbutton
checkVar = tk.BooleanVar()
check1 = ttk.Checkbutton(
    master=window,
    text = "text box 1",
    command = lambda: print(checkVar.get()),
    variable=checkVar
)
check1.pack()

checkVar2 = tk.BooleanVar()
check2 = ttk.Checkbutton(
    master=window,
    text = "text box 1",
    command = lambda: print(checkVar2.get()),
    variable=checkVar2
)
check2.pack()

#radioButtons
radioVar = tk.StringVar()
radio1 = ttk.Radiobutton(
    master=window,
    text = "Radio Button 1",
    value = 'btn 1',
    variable = radioVar,
    command=print(radioVar.get()),
)
radio1.pack()
radio2 = ttk.Radiobutton(
    master=window,
    text = "Radio Button 2"
    ,value = 2,
    variable = radioVar,
    command=print(radioVar.get())  ,
)
radio2.pack()

def chk3_clicked():
    print("chkbox clicked")
    print(f"rdo>{myRadioVar.get()}<---")


def rdo_clicked():
    print("rdo clicked")
    checkVar3.set(False)

checkVar3 = tk.BooleanVar()
check3 = ttk.Checkbutton(
    master=window,
    text = "text box 1",
    command = chk3_clicked,
    variable=checkVar3
)
check3.pack()

myRadioVar = tk.StringVar()
radioA = ttk.Radiobutton(
    master=window,
    text = "Radio A",
    value = 'A',
    variable = myRadioVar,
    command=rdo_clicked
)
radioA.pack()
radioB = ttk.Radiobutton(
    master=window,
    text = "Radio B",
    value = 'B',
    variable = myRadioVar,
    command=rdo_clicked
)
radioB.pack()







#run
window.mainloop()
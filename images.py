import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def changeViewMode():
    choice = radioBtnVar.get()
    if ( choice == 'Stretch Image'):
        canvas.bind('<Configure>', stretch_image)
    elif choice == 'Fill Image':
        canvas.bind('<Configure>', fill_image)        
    else:
        canvas.bind('<Configure>', show_full_image)
    canvas.configure(width=100, height=100)

def stretch_image(event):
    global resizedTk
    #size
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    canvas.delete("all")    
    print(f"{width}x{height}")

    #create an image
    resizedImage = image_original.resize((width,height))
    resizedTk = ImageTk.PhotoImage(resizedImage)
    canvas.create_image(
        0,0,
        image=resizedTk,
        anchor='nw'
    )

def fill_image(event):
    global resized_tk
    event_width = canvas.winfo_width()
    event_height = canvas.winfo_height() 
    canvas.delete("all")       
    canvas_ratio = event_width/ event_height
    if canvas_ratio > image_ratio:   #canvas is wider than the image
        width = int(event_width)
        height = int(width / image_ratio)
    else:  #canvas is narrorwer than the image
        height = int(event_width)
        width = int(height*image_ratio)

    resized_image = image_original.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event_width/2),
        int(event_height/2),
        anchor='center',
        image=resized_tk)


def show_full_image(event):
    global resized_tk
    event_width = canvas.winfo_width()
    event_height = canvas.winfo_height()        
    canvas_ratio = event_width/ event_height
    canvas.delete("all")
    print(f"canvas:{canvas_ratio} image:{image_ratio}")
    if canvas_ratio > image_ratio:   #canvas is wider than the image
        height = int(event_height)
        width = int(height*image_ratio)
    else:  #canvas is narrorwer than the image
        width = int(event_width)
        height = int(width / image_ratio)        

    resized_image = image_original.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(
        int(event_width/2),
        int(event_height/2),
        anchor='center',
        image=resized_tk)

#setup 
window = tk.Tk()
window.geometry('600x400')
window.minsize(318,237)
window.title('Images')

#grid layout
window.columnconfigure((0,1,2,3), weight=1, uniform='a')
window.rowconfigure((0), weight=1, uniform='a')

#import an image
image_original = Image.open('images/raccoon.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('images/python_dark.png').resize((30,30))
pyDarkTk = ImageTk.PhotoImage(python_dark)



imgCtk = ctk.CTkImage(
    light_image = Image.open('images/python_dark.png'),
    dark_image = Image.open('images/python_light.png'),
)
#widget
"""
label = ttk.Label(
    window, 
    text='racoon',
    image=image_tk
)
label.pack()
"""

buttonFrame = ttk.Frame(window)

button= ttk.Button(
    buttonFrame, 
    text = '  a button', 
    image= pyDarkTk,
    compound = 'left'
    ).pack(pady=10)

buttonCtk= ctk.CTkButton(
    buttonFrame, 
    text = '  a button', 
    image= imgCtk,
    compound = 'left'
    ).pack(pady=10)


radioBtnVar = tk.StringVar()
rdoStretch = ctk.CTkRadioButton(
    buttonFrame,
    text='Stretch',
    value = 'Stretch Image',
    variable = radioBtnVar,
    #command=changeViewMode,
)
rdoStretch.pack(pady=10)
rdoStretch.bind("<Button-1>", stretch_image)

rdoFill = ctk.CTkRadioButton(
    buttonFrame,
    text='Fill ',
    value = 'Fill Image',
    variable = radioBtnVar,    
    #command=changeViewMode,
)
rdoFill.pack(pady=10)
rdoFill.bind("<Button-1>", fill_image)

rdoFull = ctk.CTkRadioButton(
    buttonFrame,
    text='Full ',
    value='Full Image',
    variable = radioBtnVar,    
    #command=changeViewMode,
)
rdoFull.pack(pady=10)
rdoFull.bind("<Button-1>", show_full_image)

radioBtnVar.set("Full Image")

buttonFrame.grid(row=0, column=0, sticky='news')

#canvas -> image
canvas = tk.Canvas(
    window, 
    #background='red',
    bd=0,
    highlightthickness=0,
    relief='ridge',
)
canvas.grid(column=1, columnspan=3, row=0, sticky="news")
canvas.bind('<Configure>', show_full_image)

#run
window.mainloop()
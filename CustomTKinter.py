import tkinter as tk
from tkinter import ttk
import customtkinter as ctk 
"""
GitHub  TomSchimansky/CustomTKinter for documentation of CTK
"""
#window
window = ctk.CTk()
window.title("customtkinter app")
window.geometry("600x400")



#widgets
string_var = ctk.StringVar(value='a custom string')
label = ctk.CTkLabel(
    window, 
    text='A CTK Label',
    fg_color=('blue', 'red'),
    text_color=('red','blue'),
    corner_radius = 10,
    textvariable = string_var
    )
label.pack()

btnDark = ctk.CTkButton(
    window,
    text='DarkMode',

    text_color = "#000",
    hover_color='#AA0',
    command = lambda: ctk.set_appearance_mode('dark')
)
btnDark.pack()

btnLight = ctk.CTkButton(
    window,
    text='LightMode',
    fg_color="#FF0",
    text_color = "#000",
    hover_color='#AA0',
    command = lambda: ctk.set_appearance_mode('light')
)
btnLight.pack()

frame = ctk.CTkFrame(window, fg_color='green')
frame.pack()
slider = ctk.CTkSlider(frame)
slider.pack(padx=2, pady=20)

switch = ctk.CTkSwitch(
    master=window,
    text='CTkSwitch',
    corner_radius=2,
    switch_height=30,
    switch_width=60,
    border_width=3,
    fg_color='red',
    progress_color='pink',    
    button_color='green',
    border_color='blue',
    button_hover_color='yellow',
)
switch.pack()

window.attributes("-topmost",True)
window.mainloop()



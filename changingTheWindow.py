import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('More on the window')
#window.geometry('640x480')
w=640
h=480
x = window.winfo_screenwidth() // 2 - (w//2)
y = window.winfo_screenheight() // 2 - (h//2)

geom =f"640x480+{x}+{y}"
print(geom)
window.geometry(geom)

"""
window.maxsize(
    width=800,
    height=700
)
"""
window.resizable(True, True)

#screen sizes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attributes
#window.attributes('-alpha',0.01 )
#window.attributes("-topmost", True)

#security event
window.bind("<Escape>", lambda event: window.quit())

#window.attributes("-fullscreen", True)
#window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')

window.mainloop()
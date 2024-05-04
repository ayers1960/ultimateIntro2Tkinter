import tkinter as tk
from tkinter import ttk

#setup 
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')




#canvas
canvas = tk.Canvas(
    master = window,
    bg='white'
)
canvas.pack()
"""
canvas.create_rectangle(50,20,100,200, fill='red', 
                        width=10, outline='green')

canvas.create_line((0,0,200,150), fill='blue')

canvas.create_oval((200,0,300,100), fill='white')
canvas.create_arc((200,0,300,100), fill='gray', 
                    start=45,extent=180, style=tk.ARC, outline='red')


canvas.create_polygon(200,200, 100,200, 300,50)

canvas.create_text(200,250, 
text='hi mom', fill='green', width=10, )

canvas.create_window(
    (225,250), 
    window = ttk.Button( window, text='text in a canvas')
)
"""
canvas.create_line((0,0,0,0), fill='blue')


def updateLine(event):
    global brush_size
    x = event.x
    y = event.y
    canvas.create_oval(
        (
            x - brush_size/2,
            y + brush_size/2,
            x + brush_size/2,
            y + brush_size/2
        ),
        fill='green'
    )

def brush_size_adjust(event):
    global brush_size
    print(event)
    print(brush_size)
    print(event.state)
    if event.state < 1000:
        brush_size += 1
    else:
        brush_size -= 1
    brush_size = max(0,min(brush_size,50))

def brush_mouse(event):
    print(event)

brush_size = 4
canvas.bind("<Motion>",updateLine)
canvas.bind("<B1-Motion>", brush_size_adjust)
canvas.bind("<B3-Motion>", brush_size_adjust)
canvas.bind("<MouseWheel>", brush_mouse)
#run
window.mainloop()
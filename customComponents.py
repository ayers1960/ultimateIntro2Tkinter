import tkinter as tk
from tkinter import ttk

def create_segment(parent, lblText, btnText):
    frame = ttk.Frame(master=parent)
    frame.rowconfigure(0,weight = 1)
    frame.columnconfigure((0,1,2), weight=1, uniform='a')

    ttk.Label(frame, text=lblText).grid(row=0, column=0, sticky='news')
    ttk.Button(frame, text=btnText).grid(row=0, column=1, sticky='news')    
    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, lbltext, btnText,entryBtn):
        super().__init__( master=parent )
        self.rowconfigure(0,weight = 1)
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        ttk.Label(self, text=lbltext).grid(row=0, column=0, sticky='news')
        ttk.Button(self, text=btnText).grid(row=0, column=1, sticky='news')
        self.thirdColumn(entryBtn).grid(row=0, column=2, sticky='news')
        self.pack( expand=True, fill='both', padx=10, pady=10)

    def thirdColumn(self, btnLbl):
        frame = ttk.Frame(self)
        ttk.Entry(frame,).pack(expand=True, fill='both')
        ttk.Button(frame,text=btnLbl).pack(expand=True, fill='both')
        return frame


window = tk.Tk()
window.title('Widges and return')
window.geometry('400x600')

#widgets
"""
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
"""
Segment(window, 'label', 'button','one')
Segment(window, 'test', 'click','two')
Segment(window, 'hello', 'test', 'three')
Segment(window, 'test', 'click','four')
lastOne = Segment(window, 'exit', 'ttfn','five')


#run
window.mainloop()

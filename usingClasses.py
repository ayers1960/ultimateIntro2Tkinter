import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, geo):
        
        #main setup
        super().__init__()
        self.title = (title)
        self.defaultX = geo[0]
        self.defaultY = geo[1]
        self.geometry(f"{self.defaultX}x{self.defaultY}")
        self.minsize(self.defaultX, self.defaultY)

        #widgets
        self.menu = Menu(self)
        self.main = Main(self)
        #run the app
        self.mainloop()


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(
            relx=0.3,
            y=0, 
            relwidth=0.7,
            relheight=1,) 
        self.frameL = self.mainFrameClass(self, "LABEL1", 'green', "BUTTON-1")
        self.frameR = self.mainFrameClass(self, "Label2", 'orange', "Button-2")


    class mainFrameClass(ttk.Frame):
        def __init__(self,parent, lblText, lblColor, btnText):
            super().__init__(parent)
            label = ttk.Label(self, text=lblText, background=lblColor)
            button = ttk.Button(self, text=btnText)
            label.pack(expand=True, fill='both')
            button.pack(expand=True, fill='both', pady=10)        
            self.pack(side='left', expand=True, fill='both', padx=10, pady=10)


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(
            x=0,
            y=0, 
            relwidth=0.3,
            relheight=1,
        )
        self.create_widgets()

    def create_widgets(self):
        menu_button1 = ttk.Button(self, text='Button 1')
        menu_button2 = ttk.Button(self, text='Button 2')
        menu_button3 = ttk.Button(self, text='Button 3')

        menu_slider1 = ttk.Scale(self, orient='vertical')
        menu_slider2 = ttk.Scale(self, orient='vertical')


        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text='check 1')
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text='check 2')

        entry = ttk.Entry(self)        


        #menu layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1 , uniform='a')

        menu_button1.grid(row=0, column=0, sticky='NEWS', columnspan=2)
        menu_button2.grid(row=0, column=2, sticky='NEWS', )
        menu_button3.grid(row=1, column=0, sticky='NEWS', columnspan=3)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky='news', pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky='news', pady=20)

        #toggle_layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky='news')
        menu_toggle1.pack(side='left', expand=True)
        menu_toggle2.pack(side='left', expand=True)

        #entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')


App('Class Based App',(640,640))

import tkinter as tk
from tkinter import ttk
from random import randint, choice
from datetime import datetime
import pprint

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand = True, fill='both')

        #attibutes
        self.text_data = text_data
        self.item_number = len(self.text_data)
        self.list_height = item_height * self.item_number

        #canvas
        l = 0
        t = 0

        self.b = self.list_height
        self.canvas = tk.Canvas(
            self, 
            background = 'pink',
            scrollregion=(l,t,self.winfo_width(),self.b)
        )
        self.canvas.pack(expand=True, fill='both')

        #display frame
        self.frame = ttk.Frame(self)
        for index,item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both')
            
        self.bind('<Configure>',self.update_size)

        self.scrollbar = ttk.Scrollbar(self, orient='vertical',command=self.canvas.yview)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)


    def update_size(self,event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all("<Button-4>", lambda event: self.mouseMovement(event)) 
            self.canvas.bind_all("<Button-5>", lambda event: self.mouseMovement(event))                
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')                    
        else:
            height=self.winfo_height()
            self.canvas.unbind_all("<Button-4>")
            self.scrollbar.place_forget()
          
        self.canvas.create_window( 
                    (0,0), 
                    window = self.frame, 
                    anchor='nw', 
                    width=self.winfo_width(), 
                    height=height,
                )

    def create_item(self,index,item):
        frame = ttk.Frame(self.frame)
        #grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2,3,4), weight=1,uniform='1')
        #widgets
        ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='news')

        return frame

    def mouseMovement(self,event):

        if event.state == 0 and event.num == 4:
            self.canvas.yview_scroll(-5, "units")
        elif event.state == 0 and event.num == 5:
            self.canvas.yview_scroll(5, "units")

        if event.state == 4 and event.num == 4:
            self.canvas.xview_scroll(-10, "units")
        elif event.state == 4 and event.num == 5:
            self.canvas.xview_scroll(10, "units")        
    

#setup 
window = tk.Tk()
window.geometry('500x400')
window.title('Scrollable Widgets')
text_list = [
    ('label', 'button'), 
    ('thing', 'click'), 
    ('third', 'something'), 
    ('label', 'button'), 
    ('labe2', 'button2'), 
]
list_frame = ListFrame(window,text_list, 100)

window.attributes("-topmost",True)
window.mainloop()

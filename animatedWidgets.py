import customtkinter as ctk
from random import choice

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, startPos, endPos):
        super().__init__(master=parent)
        self.startPos = startPos+0.04
        self.endPos = endPos - 0.03
        self.width = abs(startPos - endPos)
        
        #animation logic
        self.pos = self.startPos
        self.in_start_pos = True


        #layout
        self.place(relx=self.startPos, rely=0.05, relwidth=self.width, relheight=0.90)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.endPos:
            self.pos  -= 0.008
            self.place(relx=self.pos,  rely=0.05, relwidth=self.width, relheight=0.90)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.startPos:
            self.pos  += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.90)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

    def flipSidebar(self):
        print(f"flip {self.startPos}")
        self.pos = self.startPos   
        if ( self.startPos > 0.5 ):
            self.startPos = 0
            self.endPos   = -0.3
            self.in_start_pos = True            
        else:
            self.startPos = 1
            self.endPos = 0.75
            self.in_start_pos = False
        self.animate()
        """
        tmp =  self.startPos 
        self.startPos =self.endPos
        self.endPos = tmp
        self.anchor()
        """

def infinite_print():
    global button_x
    button_x += 0.01
    print(f'infinite  {button_x:.03}')
    #configure
    colors = ['red', 'yellow', 'pink', 'green', 'blue','purple', 'white', 'black']
    color = choice(colors)
    button.configure(fg_color=color)   
    button.place(relx=button_x, rely=0.5, anchor='center')
    if ( button_x < 0.9) :
        window.after(50, infinite_print)

def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, anchor='center')

    #configure
    colors = ['red', 'yellow', 'pink', 'green', 'blue','purple', 'white', 'black']
    color = choice(colors)
    button.configure(fg_color=color)



#window 
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('640x480')

#animated widget
#animatedPanel = SlidePanel(window,1, .75)
animatedPanel = SlidePanel(window,0,-0.3)
ctk.CTkLabel(
    animatedPanel, text='Label 1'
    ).pack(
        expand=True, fill='both'
    )
ctk.CTkLabel(
    animatedPanel, text='Label 2'
    ).pack(
        expand=True, fill='both'
    )
ctk.CTkButton(
    animatedPanel, text='Flip Sidebar', 
    corner_radius=0, command=animatedPanel.flipSidebar
    ).pack(
        expand=True, fill='both', pady=15,

    )    
ctk.CTkTextbox(
    animatedPanel, 
    fg_color=('#dbdbdb', '#2b2b2b')).pack(
        expand='True', fill='both',pady=5
    )

#button
button_x = 0.01
button = ctk.CTkButton(
    window,
    text = 'toggle sidebar',
    command = animatedPanel.animate
)
button.place(relx=.50, rely=0.5,  anchor='center')

#run 
window.attributes("-topmost",True)
window.mainloop()
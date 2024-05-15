import customtkinter as ctk 
import settings as S
try: 
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    def __init__(self):

        #window setup 
        super().__init__(fg_color=S.APP_COLOR)
        self.title("")
        #self.iconbitmap('empty.ico')
        self.geometry('400x400')
        self.resizable(False,False)

        self.change_title_bar_color()

        self.columnconfigure(0,weight=1)
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')

        #data
        self.metric_bool = ctk.BooleanVar(value=True)
        self.height_int = ctk.IntVar(value = 170)
        self.weight_float = ctk.DoubleVar(value=60)
        self.bmiResult = ctk.StringVar()
        self.updateBMI()

        #tracing
        self.height_int.trace('w', self.updateBMI)
        self.weight_float.trace('w', self.updateBMI)
        self.metric_bool.trace('w', self.change_units)
      

        #widgets
        self.ResultText   = ResultText(self, self.bmiResult)
        self.WeightInput  = WeightInput(
            self, 
            self.weight_float,
            self.metric_bool,
        )
        self.HeightInput  = HeightInput(
            self, 
            self.height_int,
            self.metric_bool,
        )
        self.UnitSwitcher = UnitSwitcher(self, self.metric_bool)

        ctk.set_appearance_mode("dark") 
        self.mainloop()

    def change_units(self, *args):
        self.HeightInput.update_text(self.height_int.get())
        self.WeightInput.update_weight(None)

    def updateBMI(self, *args):
        # bmi = weightkg/height_meter^2
        height_meter = self.height_int.get()/100
        weight_kg    = self.weight_float.get()
        bmi = round(weight_kg / ( height_meter**2),2)
        self.bmiResult.set( f"{bmi}")

    def change_title_bar_color(self):
        """ only works on window """
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE=35
            COLOR = S.TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR, sizof(c_int))))
        except:
            pass

class ResultText(ctk.CTkLabel):
    def __init__(self,parent, bmiResult):
        self.font = ctk.CTkFont(
            S.FONT, 
            size=S.MAIN_TEXT_SIZE,
            weight='bold',
        )
        super().__init__(
            master=parent, 
            text=22.5, 
            font=self.font,
            text_color=S.WHITE,   
            textvariable = bmiResult,      
        )
        self.grid( column=0, row=0, rowspan=2, sticky='nsew')

class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float, metric_bool):
        super().__init__(master=parent, fg_color=S.WHITE)
        self.grid(column=0, row=2, sticky='news', padx=10, pady=10)
        self.weight_float = weight_float
        self.metric_bool = metric_bool        
        #layout
        self.rowconfigure(0,weight=1, uniform='b')
        self.columnconfigure(0, weight=2, uniform = 'b')
        self.columnconfigure(1, weight=1, uniform = 'b')
        self.columnconfigure(2, weight=3, uniform = 'b')
        self.columnconfigure(3, weight=1, uniform = 'b')
        self.columnconfigure(4, weight=2, uniform = 'b')

        #text widget
        self.font = ctk.CTkFont( family=S.FONT, size=S.INPUT_FONT_SIZE)
        self.labelStrVar = ctk.StringVar()
        self.label = ctk.CTkLabel(
            self, 
            textvariable = self.labelStrVar,
            text_color=S.BLACK,
            font=self.font,
        )
        self.update_weight()
        self.label.grid(row=0, column=2, )

        #buttons
        self.minus_button = ctk.CTkButton(
            self, text = '-', 
            font = self.font,
            text_color=S.BLACK,
            fg_color=S.LIGHT_GRAY,
            hover_color=S.GRAY,
            corner_radius=S.BUTTON_CORNER_RADIUS,
            command=lambda: self.update_weight(('minus','large')),
        )
        self.minus_button.grid(row=0, column=0, sticky='NS', padx=8, pady=8)

        self.smallMinus_button = ctk.CTkButton(
            self, text = '-', 
            font = self.font,
            text_color=S.BLACK,
            fg_color=S.LIGHT_GRAY,
            hover_color=S.GRAY,
            corner_radius=S.BUTTON_CORNER_RADIUS,
            command=lambda: self.update_weight(('minus','small')),            
        )
        self.smallMinus_button.grid(row=0, column=1, padx=4, pady=4)  

        self.smallPlus_button = ctk.CTkButton(
            self, text = '+', 
            font = self.font,
            text_color=S.BLACK,
            fg_color=S.LIGHT_GRAY,
            hover_color=S.GRAY,
            corner_radius=S.BUTTON_CORNER_RADIUS,
            command=lambda: self.update_weight(('plus','small')),            
        )
        self.smallPlus_button.grid(row=0, column=3, padx=4, pady=4)  


        self.plus_button = ctk.CTkButton(
            self, text = '+', 
            font = self.font,
            text_color=S.BLACK,
            fg_color=S.LIGHT_GRAY,
            hover_color=S.GRAY,
            corner_radius=S.BUTTON_CORNER_RADIUS,
            command=lambda: self.update_weight(('plus','large')),            
        )
        self.plus_button.grid(row=0, column=4, sticky='NS', padx=8, pady=8)      

    def update_weight(self, info=None):  
        if ( info is not None ) :
            if info[1] == 'large':
                amount = 1
            else:
                amount = 0.1
            if ( info[0] == 'minus'):
                self.weight_float.set(self.weight_float.get()-amount)
            else:
                self.weight_float.set(self.weight_float.get()+amount)
        if self.metric_bool.get():              
            unit = 'kg'
            weight = f"{self.weight_float.get():0.1f}"
        else:
            unit = 'lb'
            weight = f"{self.weight_float.get()/0.4536:0.1f}"
        self.labelStrVar.set(f"{weight}{unit}")

class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int, metric_bool):
        super().__init__(master=parent, fg_color=S.WHITE)
        self.grid(row=3,column=0, sticky='news', padx=10, pady=10)

        self.metric_bool = metric_bool
        #widgets
        self.slider = ctk.CTkSlider(
            self, 
            command = self.update_text,
            button_color=S.APP_COLOR,
            button_hover_color=S.GRAY,
            progress_color=S.APP_COLOR,
            fg_color=S.LIGHT_GRAY,
            variable=height_int,
            from_ = 100,
            to=250,
        )
        self.slider.pack(side='left', fill='x', expand='True', padx=10, pady=10)
        self.output_string = ctk.StringVar()
        self.outputText = ctk.CTkLabel(
            self,
            text_color=S.BLACK,
            font = ctk.CTkFont(family=S.FONT,size=S.INPUT_FONT_SIZE),
            textvariable = self.output_string,
        )
        self.update_text(height_int.get())
        self.outputText.pack(side='left', padx=20)

    def update_text(self, amount):

        if self.metric_bool.get():
            unit='M'
            self.output_string.set(f"{amount/100:0.2f}{unit}")
        else:
            inchesAmount = round(amount /2.54)
            feet = inchesAmount // 12
            inches = inchesAmount % 12
            self.output_string.set(f"{feet}'{inches}\"")       
             
class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent, metric_bool):
        super().__init__(
            master=parent, 
            text='metric',
            text_color = S.SWITCH_TEXT_COLOR,
            font = ctk.CTkFont(family=S.FONT,size=S.SWITCH_FONT_SIZE, weight='bold'),
        )
        self.metric_bool = metric_bool        
        self.bind("<Button>", self.change_units)
        self.place(
            relx=0.98,
            rely=0.01,
            anchor='ne')

    def change_units( self, event):
        self.metric_bool.set(not self.metric_bool.get())
        if self.metric_bool.get():
            self.configure(text='metric')
        else:
            self.configure(text='imperial')


if __name__ == '__main__':
    App()

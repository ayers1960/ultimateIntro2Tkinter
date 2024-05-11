
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter
#window 
window = ttk.Window(themename='darkly')
window.title('extra widgets')

#scrollable frame
scrollFrame = ScrolledFrame(window)
scrollFrame.pack(expand=True,fill='both')

for i in range(100):
    ttk.Label(scrollFrame, text = f"Label:{i}").pack(fill='x')
    ttk.Button(scrollFrame, text = f"Button:{i}").pack(fill='x')
    ttk.Separator(scrollFrame, orient='horizontal').pack(expan=True, fill='both')


#toast

toast = ToastNotification(
    title = 'this is a message title',
    message = 'this is the actual message',
    duration = 600,
    bootstyle='dark',
    position = (50,100,'ne'),
)
ttk.Button(window, text ='show toast', command = toast.show_toast).pack()

# tooltip
button = ttk.Button(
    window, 
    text = 'tool tip button',
    bootstyle = 'warning'
).pack(pady=10)
##ToolTip(button, text='this does something')


##calendar
calendar = DateEntry(window)
calendar.pack(pady=10)
ttk.Button(
    window, 
    text = 'print calender date', 
    command = lambda: print(calendar.entry.get())
).pack()

# progress --> floodgauge
progressInt = tk.IntVar(value=50)
progress = ttk.Floodgauge(
    window,
    text = 'progress',
    variable = progressInt,
    bootstyle='danger',
    mask = 'mask {}%'
).pack(pady=10, fill='x')

ttk.Scale(
    window, 
    from_=0,
    to=100,
    variable=progressInt
).pack()

meter = ttk.Meter(
    metersize=180,
    padding=5,
    bootstyle='danger',
    interactive=True,
    textleft='to the left',
    subtext = 'some subtext',
    metertype = 'full'
)
meter.pack()


#run 
window.attributes("-topmost",True)
window.mainloop()
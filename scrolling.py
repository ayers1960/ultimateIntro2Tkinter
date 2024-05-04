import tkinter as tk
from tkinter import ttk
from random import randint, choice
from datetime import datetime
import pprint



def mouseMovement(event):

    if event.state == 0 and event.num == 4:
        canvas.yview_scroll(-5, "units")
    elif event.state == 0 and event.num == 5:
        canvas.yview_scroll(5, "units")

    if event.state == 4 and event.num == 4:
        canvas.xview_scroll(-10, "units")
    elif event.state == 4 and event.num == 5:
        canvas.xview_scroll(10, "units")        
    


#setup 
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

"""
#canvas
canvas = tk.Canvas(window,bg='lightgray', scrollregion=(0,0,2000,5000))
canvas.pack(expand=True, fill='both')
canvas.create_line(0,0,2000,5000, fill='green', width=10)

for i in range(10):
    l = randint(0,2000)
    t = randint(0, 5000)
    r = randint(10,500)
    b = randint(10,500)
    color = choice(('red', 'blue','yellow', 'orange', 'black'))
    canvas.create_rectangle(l,t,r,b,fill=color)

#mousewheel scrolling
canvas.bind_all('<MouseWheel>', lambda event: lambda event: canvas.yview_scroll(int(event.delta/60), "units"))
canvas.bind("<Button-4>", lambda event: mouseMovement(event))
canvas.bind("<Button-5>", lambda event: mouseMovement(event))
canvas.bind("<Control-Button-5>", lambda event: mouseMovement(event))
canvas.bind("<Control-Button-5>", lambda event: mouseMovement(event))

#scrollbar
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
canvas.configure(yscrollcommand=scrollbar.set)

hScrollBar = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
hScrollBar.place(relx=0, rely=1, relwidth=1, anchor='sw')
canvas.configure(xscrollcommand=hScrollBar.set)
"""

"""
#text 
text = tk.Text(window)
for i in range(1,200):
    str=f"TEXT ({i}):"
    for k in range(1,200):
        str += f"{k} "
    str += "\n"
    text.insert(f'{i}.0', str)
text.pack( expand=True, fill='both')

scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')
text.configure(yscrollcommand=scrollbar_text.set)
"""

table = ttk.Treeview(window, columns = (1,2,3,4,5,6,7,8,9,10), show='headings')
for i in range(1,10):
    table.heading(i, text = f"NAME:{i}")
#table.heading(1, text = "First Name")
#table.heading(2, text = 'Last Name')
first_names = ['Laura', 'Luella', 'Latisha', 'Sam', 'Edgar', 'Mary', 'Larry', 'Megan', 'Kathleen', 'Mike', 'Anne', 'Leigh']
last_names = ['Crockett', 'Howell', 'Ayers', 'Warren']
for i in range(100):
    names = []
    for k in range(1,10):
        names.append(f"{choice(first_names)} {choice(last_names)}")
    table.insert(parent='', index=tk.END,
                values=(names))
table.pack(expand=True, fill='both')


scrollbar_tree = ttk.Scrollbar(window, orient='vertical', command=table.yview)
scrollbar_tree.place(relx=1, rely=0, relheight=1, anchor='ne')
table.configure(yscrollcommand=scrollbar_tree.set)

scrollbar_treeH = ttk.Scrollbar(window, orient='horizontal', command=table.xview)
table.configure(xscrollcommand=scrollbar_treeH.set)
scrollbar_treeH.place(relx=0, rely=1,relwidth=1, anchor='sw' )

window.attributes("-topmost",True)
window.mainloop()

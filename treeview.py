import tkinter as tk
from tkinter import ttk
from random import choice

#window
window = tk.Tk()
window.geometry("640x480")
window.title("Treeview")

#data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Latisha']
last_names  = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook','Taylor', 'Walker', 'Clark']

#treeview
table = ttk.Treeview(
    master = window,
    columns=('first', 'last','email'), 
    show = 'headings',
)
table.pack(fill='both', expand=True)
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='E-Mail')

#insert values into a table
#table.insert( parent = '', index = 0, values = ('john','doe','jd@email.com'))
for i in range(100):
    fn = choice(first_names)
    ln = choice(last_names)
    em = f"{fn[:3]}{ln}@myorg.org"    
    data = (fn,ln,em)
    table.insert( 
        parent = '', 
        index = 0, 
        values = data
    )

table.insert(
    parent = '', 
    index = tk.END,
    values=('xxx','yyy','zzz')
)

#events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(f"{i}:{table.item(i)['values']}")

def delete_items(_):
    print('delete')
    for i in table.selection():
        print(f"{i}:{table.item(i)['values']}")
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select )
table.bind('<Delete>', delete_items)
#items


#run
window.mainloop()
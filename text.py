import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

root = tk.Tk()
style = ttk.Style(root)
# create custom DateEntry style with red background
style.configure('my.DateEntry', fieldbackground='red')
# create DateEntry using the custom style
dateentry = DateEntry(root, style='my.DateEntry') 
dateentry.pack()

root.mainloop()
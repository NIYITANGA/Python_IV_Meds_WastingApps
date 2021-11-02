from tkinter import *
from tkinter import ttk
import pandas as pd

root = Tk()

root.geometry("100x70")
# creating DataFrame
df = pd.DataFrame({'Name': ['Chetan', 'yashas', 'yuvraj', 'Pooja', 'Sindu', 'Renuka'], 'Age': [20, 25, 30, 18, 25, 20],
                   'Height': [155, 160, 175, 145, 155, 165], 'Weight': [75, 60, 75, 45, 55, 65]})

print(df)

largest_items = df.nlargest(3)
data_label = Label(root, text=str(largest_items))
data_label.pack()

root.mainloop()
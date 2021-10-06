# import tkinter and all its functions

from tkinter import *
from tkinter import ttk
from tkmacosx import Button as button
from tkcalendar import DateEntry


# define command functions

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['value'][0])
    t2.set(item['value'][1])
    t3.set(item['value'][2])
    t4.set(item['value'][3])
    t5.set(item['value'][4])


#Striped Treeview Rows with color

    trv.tag_configure("evenrow", background='white', foreground='green')
    trv.tag_configure("oddrow", background='green', foreground='white')


count = 1
def update_wastedItemsList():

   global count 
   
   i=count

   if i % 2 == 0:

        trv.insert(parent='', index='end' , text="", values= (count, ent2.get(), ent3.get(), ent4.get(), ent5.get()), tags=('evenrow',)) 
    
   else:

          trv.insert(parent='', index='end' , text="", values= (count, ent2.get(), ent3.get(), ent4.get(), ent5.get()), tags=('oddrow',)) 
    

   count = count + 1


# Remove one selected item from the IV_Meds wasted list

def Remove_oneItemFromList():
    D = trv.selection()[0]
    trv.delete(D)

# Remove  more than one selected items from the IV_Meds wasted list

def Remove_moreItemFromList():
    D = trv.selection()
    for record in D:
        trv.delete(record)
    

def delete_AllItem():
    for record in trv.get_children():
         trv.delete(record)
    

# create root window
root = Tk()


# create t1, t2, t3, t4

t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()


#Title of GUI Window

root.title("IV_WastingApps") 

# Specify the max size the window can exand to

root.geometry("1430x750")

#Specify background color

root.config(bg="grey")

#Create left and right frames

wrapper = LabelFrame(root, width=700)
wrapper.grid(row=0, column=0)
wrapper3 = LabelFrame(root, width=700, height=760, text="Wasted IV_Meds Data Visualition", bg="lightgrey", font=("Helvetica", 15))
wrapper3.grid(row=0, column=1)

# Create wrappers and labels in left_frame

wrapper1 = LabelFrame(wrapper, width=700, height=450, text="IV_Meds wasted list", bg="lightgrey", font=("Helvetica", 15))
wrapper1.grid(row=0, column=0)
wrapper2 = LabelFrame(wrapper, text="Wasting IV_Meds Portal", bg="lightgrey", font=("Helvetica", 15))
wrapper2.grid(row=2, column=0)


# create treeview inside the IV_MedS Wasted list wrapper

style = ttk.Style()
trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height=15)
vsb = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
vsb.pack(side ='right', fill ='x')
trv.configure(xscrollcommand=vsb.set)
style.configure("Treeview.Heading", font=("Helvetica", 14))

#Configure treeview colors

style.configure("Treeview", background="lightblue", forgound="black", rowheight=25, fieldbackground="silver")
trv.pack()

#Change the color of selected row in treeview

style.map('Treeview', background=[('selected', 'gray')])

#Create striped row tags

trv.column("#1", anchor=CENTER, width=40)
trv.column("#2", width=240)
trv.column("#3", anchor=CENTER, width=140) 
trv.column("#4", anchor=CENTER, width=140)
trv.column("#5", anchor=CENTER, width=140)

trv.heading(1, text="Index")
trv.heading(2, text="Drug's Name")
trv.heading(3, text="Wasted Number")
trv.heading(4, text="Wasted Money $")
trv.heading(5, text="Date")


# create Wasting IV_Meds Portal

IV_Meds = [
    "vancomycin",
    "meropenem",
    "gentamicin",
    "micafungin",
    "amphotericin",
    "vancomycin",
    "meropenem",
    "gentamicin",
    "micafungin",
    "amphotericin",
    "vancomycin",
    "meropenem",
    "gentamicin",
    "micafungin",
    "amphotericin"
]



lbl2 = Label(wrapper2, text="Select Item to be wasted", height=3, bg="lightgrey", font=("Helvetica", 15))
lbl2.grid(row=0, column=0, padx=5, pady=3)
ent2 = ttk.Combobox(wrapper2, value=IV_Meds, width=45, font=("Helvetica", 15))
ent2.grid(row=0, column=1, padx=14, pady=3)




lbl3 = Label(wrapper2, text="Number to be wasted", bg="lightgrey", font=("Helvetica", 15))
lbl3.grid(row=1, column=0, padx=50, pady=3)

ent3 = Entry(wrapper2, textvariable=t2)
ent3.grid(row=1, column=1, padx=5, pady=3)

lbl4 = Label(wrapper2, text="Money to be wasted $", bg="lightgrey", font=("Helvetica", 15))
lbl4.grid(row=2, column=0, padx=5, pady=3)
ent4 = Entry(wrapper2, textvariable=t3)
ent4.grid(row=2, column=1, padx=5, pady=3)

lbl5 = Label(wrapper2, text="Date", height=3, bg="lightgrey", font=("Helvetica", 15))
lbl5.grid(row=3, column=0, padx=5, pady=3)
ent5 = DateEntry(wrapper2, selectmode='day')
ent5.grid(row=3, column=1, padx=5, pady=3)



Add_btn = button(wrapper2, text="Waste an Item", command=update_wastedItemsList, bg='lightblue')
Remove_oneItem = button(wrapper2, text="Remove selected Item", command=Remove_oneItemFromList, bg='lightblue')
Remove_moreItem = button(wrapper2, text="Remove selected Items", command=Remove_moreItemFromList, bg='lightblue')
DeleteAll_btn = button(wrapper2, text="Delete All Items wasted", command=delete_AllItem, bg='lightblue')

Add_btn.grid(row=4, column= 0, padx=5, pady=10)
Remove_oneItem.grid(row=4, column= 1, padx=5, pady=10)
Remove_moreItem.grid(row=5, column=0, padx=5, pady=3)
DeleteAll_btn.grid(row=5, column=1, padx=5, pady=10)









root.mainloop()
# import tkinter and all its functions

from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkmacosx import Button as button
from tkcalendar import DateEntry
import csv
import sys
import os



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

    

count = 1
def update_wastedItemsList():

   global count 
   
   i=count

   if i % 2 == 0:

       trv.tag_configure("evenrow", background='lightgrey', foreground='black')
       
       trv.insert(parent='', index='end' , text="", values= (count, ent2.get(), ent3.get(), ent4.get(), ent5.get()), tags=('evenrow',)) 
       
       
   else:

       trv.tag_configure("oddrow", background='white', foreground='black')
       
       trv.insert(parent='', index='end' , text="", values= (count, ent2.get(), ent3.get(), ent4.get(), ent5.get()), tags=('oddrow',)) 
    
      
   count = count + 1


# Create a csv file

def Export_To_CSVFile():
    flname = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save csv", filetypes=(("csv file", "*.csv"), ("All files", "*.*")))
    with open(flname, mode='w') as Myfile:
        exp_writer = csv.writer(Myfile, delimiter=',')
        for row_id in trv.get_children():
            row = trv.item(row_id) ['values']
            exp_writer.writerow(row)

        messagebox.showinfo("Wasted IV data", "Wasted IV data has been exported to "+os.path.basename(flname)+" successfully.")


# Remove  more than one selected items from the IV_Meds wasted list

def Remove_moreItemFromList():
    D = trv.selection()
    for record in D:
        trv.delete(record)
    
count = 1
def ImportCSV():

    global count

    flname = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("csv file", "*.csv"), ("All files", "*.*")))
    with open(flname) as Myfile:
        csvread = csv.reader(Myfile, delimiter=',')
        for row in csvread:
            i=count
            if i % 2 == 0:
                trv.tag_configure("evenrow", background='lightgrey', foreground='black')
                trv.insert("", 'end', values=row, tags=('evenrow',))

            else:

                trv.tag_configure("oddrow", background='white', foreground='black')
                trv.insert("", 'end', values=row, tags=('oddrow',))


        count = count + 1
    



# Visualise the treeview contents


def Treeview_VS():

     for child in trv.get_children():

      
      

          
       

          trV.tag_configure("oddrow", background='black', foreground='white')
          
          trV.insert("",'end',text=trv.item(child)["text"],values=trv.item(child)["values"], tags=('oddrow',))


     

# Initialize root as an object for Tk() class for creating a root window.

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

root.geometry("1430x800")

#Specify background color

root.config(bg="grey")

#Create left and right frames

wrapper = LabelFrame(root, width=700)
wrapper.grid(row=0, column=0)
wrapper3 = LabelFrame(root, width=700)
wrapper3.grid(row=0, column=1)

#Create wrappers and labels in left_frame

wrapper1 = LabelFrame(wrapper, width=700, text="IV_Meds wasted list", bg="lightgrey", font=("Helvetica", 15))
wrapper1.grid(row=0, column=0)
wrapper2 = LabelFrame(wrapper, text="Wasting IV_Meds Portal", bg="lightgrey", font=("Helvetica", 15))
wrapper2.grid(row=2, column=0)

#Create wrappers and labels in right_frame

wrapper4 = LabelFrame(wrapper3, width=700, text="Top five highest IV_Meds wasted", bg="lightgrey", font=("Helvetica", 15))
wrapper4.grid(row=0, column=1)
wrapper5 = LabelFrame(wrapper3, width=700, height=496,text="Bar Chart", bg="lightgrey", font=("Helvetica", 15))
wrapper5.grid(row=2, column=1)

# create treeview inside the IV_MedS Wasted list wrapper

style = ttk.Style()
trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height=15)
vsb = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
vsb.pack(side ='right', fill ='y')
trv.configure(yscrollcommand=vsb.set)
style.configure("Treeview.Heading", font=("Helvetica", 14))

# create treeview inside the Top five highest IV_Meds wasted wrapper

style = ttk.Style()
trV = ttk.Treeview(wrapper4, columns=(1,2,3,4,5), show="headings", height=10)
vsb = ttk.Scrollbar(wrapper4, orient="vertical", command=trV.yview)
vsb.pack(side ='right', fill ='y')
trV.configure(yscrollcommand=vsb.set)
style.configure("Treeview.Heading", font=("Helvetica", 14))


# create graph



#Restart the application without closing the application windon

def restart_Apps():
    python = sys.executable
    os.execl(python, python, * sys.argv)




#Configure left treeview colors

style.configure("Treeview", background="lightblue", forgound="black", rowheight=25, fieldbackground="silver")
trv.pack()

#Configure right treeview colors

style.configure("Treeview", background="lightblue", forgound="black", rowheight=25, fieldbackground="silver")
trV.pack()

#Change the color of selected row in treeview

style.map('Treeview', background=[('selected', 'gray')])

#Create striped row tags for left treeview

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


#Create striped row tags for right treeview
trV.column("#1", anchor=CENTER, width=40)
trV.column("#2", width=200)
trV.column("#3", anchor=CENTER, width=140) 
trV.column("#4", anchor=CENTER, width=140)
trV.column("#5", anchor=CENTER, width=140)

trV.heading(1, text="Index")
trV.heading(2, text="Drug's Name")
trV.heading(3, text="Wasted Number")
trV.heading(4, text="Wasted Money $")
trV.heading(5, text="Date")

# create Wasting IV_Meds Portal

IV_Meds = [
    "vancomycin",
    "meropenem",
    "gentamicin",
    "micafungin",
    "amphotericin",
    "Cefazolin",
    "Oxytocin",
    "Insulin",
    "Thiamine",
    "Penicillin G",
    "Cefoxitin",
    "Cefepine",
    "Zosyn",
    "Mitronidazole",
    "Meropenum"
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
Export_toCSV = button(wrapper2, text="Export to CSV", command=Export_To_CSVFile, bg='lightblue')
Remove_moreItem = button(wrapper2, text="Remove selected Items", command=Remove_moreItemFromList, bg='lightblue')
ImportCVSfile = button(wrapper2, text="Import CSV File", command=ImportCSV, bg='lightblue')
Trv_Visualise = button(wrapper2, text="Sort treeview", command=Treeview_VS, bg='lightblue')
Exit_btn = button(wrapper2, text="Exit", command=root.quit, bg='white')
Restart_btn = button(wrapper2, text="Restart", command=restart_Apps, bg='lightblue')

Add_btn.grid(row=4, column= 0, padx=5, pady=10)
Export_toCSV.grid(row=4, column= 1, padx=5, pady=10)
Remove_moreItem.grid(row=5, column=0, padx=5, pady=3)
ImportCVSfile.grid(row=5, column=1, padx=5, pady=10)
Trv_Visualise.grid(row=6, column= 0, padx=5, pady=10)
Restart_btn.grid(row=6, column= 1, padx=5, pady=10)
Exit_btn.grid(row=7, columnspan=2)


# create Wasting Bar Chart window

lbl5 = Label(wrapper5, text=" Graph", height=3, bg="lightgrey", font=("Helvetica", 15))


root.mainloop()
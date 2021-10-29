# IV_Drugs wasting Apllication (IWA)

IV_Drugs wasting Application (IWA) is a python class project done by a pharmacy Technician, who has a passion of developing applications that will help pharmacy to be more profitable. 

IWA is going to help pharmacy Manager to vilualize the  data of IV_Drugs wasted, and make evidences based decisions to save money that are being wasted.

## Link

- [Repo](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps)

## This application was build with

- Python
- Tkinter

Tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

Running python -m tkinter from the command line should open a window demonstrating a simple Tk interface, letting you know that tkinter is properly installed on your system.


## Screenshots

- Home screen Layout without inputdata and output

![Home screen Layout ](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/withoutiinput.png)

- Home screen Layout with inputdata and output

![Sreen with inputdata](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/withinput.png)

## Features Included

1. First Feature: `master loop console`

As you can see on the above screeshot, this application has been designed in a way the user can repeatedly `waste an item`, `remove selected items`, `export to csv` and `import csv file`.  In additinal, the user can click on the `Restart` button to reflesh the apps and start new wasting activities. If the user want to close the application, there is possibility to do it with a simple clik on the `Exit` button.

Python function Code for waste an item;

```
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

```
 
Python function code for remove selected items;

```
 def Remove_moreItemFromList():
    D = trv.selection()
    for record in D:
        trv.delete(record)

```


Python function code for Restart;

```
 def restart_Apps():
    python = sys.executable
    os.execl(python, python, * sys.argv)

```

Python code for Exit;

```
Exit_btn = button(wrapper2, text="Exit", command=root.quit, bg='white')
```


2. Second Feature : `Usage of the object's value of created class`

One among the classes I created in this project is the `ttk.combobox`. This class has an object called `ent2`, this object has a value which is equal to `IV_Meds`. 

`
ent2 = ttk.Combobox(wrapper2, value=IV_Meds, width=45, font=("Helvetica", 15))
`

In the `def update_wastedItemsList()`, I used `ent2.get()` to get the value of object ent2 which is the Drug's name seen in the second column of the  the first Treeview(trv).

3. Third Feature : `list`

The `IV_Meds` is a list made of 10 drugs so far, and the user can select one drug when he/she is entering the data of the item that is going to be wasted

Python code for the list `IV_Meds`;

```
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
```

4. Forth Feature ; `Read data from an external file, CSV`

There is option for the user of this application to `import` the wasted IV_Meds recorded in the CSV file and populate those data in the treeview before being visualized.

Python function code for import csv file;

```
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
        
```


5. Fifth Feacture; `conversion tool`

After the user is done exporting the data of the first treeview, there is confermation message that is poping up on the screen to conferm the name the user gave to the data file. Check the screenshot below;

![Confermation message](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/Messagebox.png)



## How to use this application


To record and visualize the data of wasted IV_Meds, the user follow the following steps. 
 - First option;
    . Select the IV_Med you want to waste by using the combobox, and enter the number of item you are going to waste with the amount of money $ the pharmacy is going to loose. Date is automaticaly populated in the `DateEntry`.
    . After entering those data, the user can click on the `sort Treeview` button to visualize the top five expensive IV_Meds wasted inside  the right treeview (trV).
    . After visualisation, the user can export (save) the IV_Meds wasted data into his/her local computer by cliking the `Export to CSV` button.

 - Second option;
    . The IV_Meds wasted data saved on the local computer by the user as csv files, could be combine together ,after one or more months, in one csv file. Then, this one csv file could be imported inside the first treeview (trv) by clicking `import csv file` button. After that, the user can visualize the combined csv file by clicking on the `sort Treeview` button.
    

To start over, the user can click on the `restart` button. Otherwise, If the user want to close the application, a simple click on `Exit` button does the action.

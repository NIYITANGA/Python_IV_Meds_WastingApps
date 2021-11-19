# IV_Drugs wasting Application (IWA)

IV_Drugs wasting Application (IWA) is a python class project done by a pharmacy Technician, who has a passion of developing applications that will make a difference in pharmacy business Intelligence. 

IWA is going to help pharmacy Manager to vilualize the  data of IV_Drugs wasted, and make evidences based decisions to save money that are being wasted.

## Link

- [Repo](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps)

## This application was build with

- Python

I used Tkinter as the de facto way in python to create Graphical User Interface (GUI) of this application. Tkinter is included with standard GNU/Linux, Microsoft Windows and macOS installs of Python.

To verify whether Tkinter is installed and ready to be loaded by Python, run the following code to test in a Python console:

```
> python

>>> import tkinter
>>> tkinter._test()

```

If Tkinter is installed and working correctly, a small popup window will appear. The first line at the top of the window should state: This is Tcl/Tk version 8.6. For more detail about python and tkinter, [click here.](https://www.activestate.com/resources/quick-reads/how-to-install-tkinter-in-windows/)


Generally, we import the tkinter library in the environment by using **`from tkinter import *`**  command.

The significance of **`import *`**  represents all the functions and built-in modules in the tkinter library. By importing all the functions and methods, we can use the inbuilt functions or methods in a particular application without importing them implicitly.

Tkinter also provides the ttk package that is used to style the widget's property and its look and feel. In order to use the ttk package, we have to import it by typing the following code −;

```
from tkinter import ttk

```
Since this Tkinter application deals wilth the file system, I have to import **`messagebox`**  and **`filedialog`**  to provide a dialog that allows file selections. Those modeles were imported by typing the following code -;

```
from tkinter import messagebox, filedialog
```

**`Tkmacosx`**  was used as a Python library extension to the Tkinter module. This change backgraound color of the button on macOS after clicking on it. To access this extension, I used the following code-;

```
from tkmacosx import Button as button
```

**`Tkcalendas`**  is an other python module. It used to provide the Calendar and DateEntry widgets for Tkinter. It was imported by the following code -;
```
from tkcalendar import DateEntr
```

To plot and visualise data, I imported **`matplotlib`**  library together with **`pyplot`**  module. In order to avoid writing the library name on every call, the alias **`plt`**  has been chosen by using the following code -;

```
import matplotlib.pyplot as plt
```

To format the plot for display in a specific target application, such as Tkinter. I imported **`FigureCanvasTkAgg`**  in the following code -;

```
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

```

The three other modules imported are ;

- **`CSV`**  to deal will csv files,
- **`SYS`**  to manipulate different parts of the Python Runtime Environment (like restarting the application) and,
- **`OS`**  to provide a way of using operating system dependent functionality (like importing and exporting data).


## Screenshots

- Home screen Layout without inputdata and output

![Home screen Layout ](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/withoutinput.png)

- Home screen Layout with inputdata and output

![Sreen with inputdata](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/withinput.png)

- Screenshot showing how to select IV_Med that is goin to be wasted

![Sreen with inputdata](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/ToselectIV.png)

## Features Included

**1. First feature: `master loop console`**

As you can see on the above screeshot, this application has been designed in a way the user can repeatedly **`waste an item`, `remove selected items`, `export to csv`** and **`import csv file`**.  In additinal, the user can click on the **`Restart`** button to reflesh the apps and start new wasting activities. If the user want to close the application, there is possibility to do it with a simple clik on the **`Exit`** button.

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


**2. Second feature : `Usage of the object's value of created class`**

One among the classes I created in this project is the **`ttk.combobox`**. This class has an object called **`ent2`**, this object has a value which is equal to **`IV_Meds`**. 

`
ent2 = ttk.Combobox(wrapper2, value=IV_Meds, width=45, font=("Helvetica", 15))
`

In the **`def update_wastedItemsList()`**, I used **`ent2.get()`** to get the value of object ent2 which is the Drug's name seen in the second column of the  the Treeview(trv).

**3. Third feature : `list`**

The **`IV_Meds`** is a list made of 15 drugs so far, and the user can select one drug when he/she is entering the data of the item that is going to be wasted. Check the screenshot above.

Python code for the list **`IV_Meds`**;

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

**4. Forth feature ; `Read data from an external file, CSV`**

There is option for the user of this application to **`import`** the wasted IV_Meds recorded in the CSV file before the end of the month, and populate those data in the treeview before being visualized.

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


**5. Fifth feacture; `conversion tool`**

After the user is done exporting the data of the first treeview, there is confermation message that is poping up on the screen to conferm the name the user gave to the data file. Check the screenshot below;

![Confermation message](https://github.com/NIYITANGA/Python_IV_Meds_WastingApps/blob/master/image/expmsage.png)


**6. Sixth feacture: `dictionary`**

To get the top 10 most expensive IV_meds from the all IV_meds wasted. I created a dictionary **`row_list.append(trv.item(child)["values"])`** from the treeview children. This dictionary was used to create a dataframe **`trv_df = pd.DataFrame(row_list, columns=columns)`** under the function **`def Treeview_VS()`**. Inside this function, I created a dataframe of the top 10 expensive IV_meds wasted; **`Top10_Expensive_wasted = trv_df.nlargest(10, 'MoneyWasted')`**. Then from this dataframe, I created another dataframe of two columns (DrungsName and MoneyWasted); **`Plotdf = Top10_Expensive_wasted[['DrugsName', 'MoneyWasted']]`**, which used to plot the bar hart of the top 10 expensive IV_meds wasted.

**7. Seventh feacture: `visualize data in bar chart`**

The users of this application can visualize the top10 most expensive IV_meds that were wasted during a certain period of time. For example, they can enter the data of the all IV_meds wasted during one month, or they can import the csv file of the all IV_meds wasted during x month. After having the data of the IV_meds wasted in the treeview, a simple click on the **`Check expensive IV_Meds Wasted`** buttom display the horizontal bar chart of the top 10 IV_meds wasted vs money wasted. This buttom is the one that is used to command the **`def Treeview_VS()`** function in the process of creating a dataframe **`Plotdf`**.

## How to use this application


**To record and visualize the data of wasted IV_Meds, the user follow the following steps.**
 - **First option;**
    - Select the IV_Med you want to waste by using the combobox, and enter the number of item you are going to waste with the amount of money $ the pharmacy is going to loose. Date is automaticaly populated in the **`DateEntry`**. After that, the user has to click on the **`waste an item`** button to complite the waste action. Before starting the visualisation, if the user finds one or more items with the wrong data in the treeview, he/she can select those items and click on **`remove selected items`** buttom to erase them from the data that are going to be visualized. When data are ready, the user can click on the **`Check expensive IV_Meds Wasted`** button to visualize the top ten expensive IV_Meds wasted on the left side.
    . To keep the records, the user can export (save) the IV_Meds wasted data into his/her local computer by cliking the **`Export to CSV`** button.

 - **Second option;**
    - The IV_Meds wasted data saved on the local computer by the user as csv files, could be combine together ,after one or more months, in one csv file. Then, this one csv file could be imported inside the treeview (trv) by clicking **`import csv file`** button. Then, the user can visualize the combined csv file by clicking on the **`Check expensive IV_Meds Wasted`** button.
    

To start over, the user can click on the **`restart`** button. Otherwise, If the user want to close the application, a simple click on **`Exit`** button does the action.

## Author

 **Theophile Niyitanga**
  - [Email](mailto:theophileca@gmail.com?subject=BUD "Hi!")

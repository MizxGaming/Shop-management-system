import mysql.connector as msql
import tkinter as tk
from tkinter import messagebox
from tkinter import font

#Connection
db = msql.connect(
    host='localhost',
    user='python',
    passwd='python',
    database='Shop',
    charset='utf8mb4',
    collation='utf8mb4_unicode_520_ci'
)
cursor = db.cursor()

#Creating necessary tables
cursor.execute("CREATE TABLE IF NOT EXISTS Products(Date DATE, prodName VARCHAR(80), prodAlias VARCHAR(20), prodPrice FLOAT(3,2));")
cursor.execute("CREATE TABLE IF NOT EXISTS Sales(custName VARCHAR(30), DOP DATE, prodName VARCHAR(80), QTY INT, prodPrice FLOAT(3,2),  TotalPrice FLOAT(3,2), MOP VARCHAR(10));")
cursor.execute("CREATE TABLE IF NOT EXISTS Bill(Name VARCHAR(30), Product VARCHAR(20), QTY INT, Price FLOAT(3,2), TotalPrice FLOAT(3,2));")


#Function to add the product to the database
def prodtoTable():
    #Getting the user inputs of product details from the user 
    pname= prodName.get()
    price = prodPrice.get()
    dt = date.get()
    #Connecting to the database
    db=msql.connect(user="python",passwd="python",host="localhost",database='Shop') 
    cursor = db.cursor()
    
    #query to add the product details to the table
    query = "INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)" 
    details = (dt,pname,price)

    #Executing the query and showing the pop up message
    try:
        cursor.execute(query,details)
        db.commit()
        messagebox.showinfo('Success',"Product added successfully")
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Error","Trouble adding data into Database")
    
    wn.destroy()
#Function to get details of the product to be added
def addProd(): 
    global prodName, prodPrice, date, Canvas1,  wn
    
    #Creating the window
    wn = wn.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = tk.Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill='both')
    
    headingFrame1 = tk.Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = tk.Label(headingFrame1, text="Add a Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Getting Date
    lable1 = tk.Label(labelFrame,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = tk.Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Product Name
    lable2 = tk.Label(labelFrame,text="Product Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    prodName = tk.Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
    # Product Price
    lable3 = tk.Label(labelFrame,text="Product Price : ", fg='black')
    lable3.place(relx=0.05,rely=0.6, relheight=0.08)
        
    prodPrice = tk.Entry(labelFrame)
    prodPrice.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
           
    #Add Button
    Btn = tk.Button(wn,text="ADD",bg='#d1ccc0', fg='black',command=prodtoTable)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    Quit= tk.Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to remove the product from the database
def removeProd():
    #Getting the product name from the user to be removed
    name = prodName.get()
    name = name.lower()
    
    #Connecting to the database
    db=msql.connect(user="python",passwd="python",host="localhost",database='Shop') 
    cursor = db.cursor()
    
    #Query to delete the respective product from the database
    query = "DELETE from products where LOWER(prodName) = '"+name+"'"
   #Executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        #cur.execute(deleteIssue)
        #con.commit()

        messagebox.showinfo('Success',"Product Record Deleted Successfully")

    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Please check Product Name")
 
    wn.destroy()
#Function to get product details from the user to be deleted
def delProd(): 

    global prodName, Canvas1,  wn
    #Creating a window
    wn = tk.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = tk.Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True,fill='both')
    
    headingFrame1 = tk.Frame(wn,bg="misty rose",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = tk.Label(headingFrame1, text="Delete Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = tk.Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Product Name to Delete
    lable = tk.Label(labelFrame,text="Product Name : ", fg='black')
    lable.place(relx=0.05,rely=0.5)
        
    prodName = tk.Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Delete Button
    Btn = tk.Button(wn,text="DELETE",bg='#d1ccc0', fg='black',command=removeProd)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = tk.Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to show all the products in the database
def viewProds():
    global  wn
    #Creating the window to show the products details
    wn = tk.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = tk.Canvas(wn) 
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True,fill='both')

    headingFrame1 = tk.Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="View Products", fg='black', font = ('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = tk.Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    #Connecting to database
    db=msql.connect(user="python",passwd="python",host="localhost",database='Shop') 
    cursor=db.cursor()
    #query to select all products from the table
    query = 'SELECT * FROM products'
    
    tk.Label(labelFrame, text="%-50s%-50s%-50s"%('Date','Product','Price'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    tk.Label(labelFrame, text = "----------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=0.2)
    #Executing the query and showing the products details
    try:
        cursor.execute(query)
        res = cursor.fetchall() 
        
        for i in res:
            tk.Label(labelFrame,text="%-50s%-50s%-50s"%(i[0],i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Failed to fetch files from database")
    
    Quit= tk.Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()

#Function to generate the bill
def bill():
    #Creating a window
    wn = tk.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='lavenderblush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = tk.Frame(wn,bg="lavenderblush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = tk.Label(headingFrame1, text="Bill", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = tk.Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.35
    tk.Label(labelFrame, text="%-40s%-40s%-40s%-40s"%('Product','Price','Quantity','Total'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    
    #Getting date and customer name
    dt=date.get()
    cName=custName.get()
    totalBill=0
    #Connecting to database
    db=msql.connect(user="python",passwd="python",host="localhost",database='Shop') 
    cursor=db.cursor()
    #query to select all the products 
    query = 'SELECT * FROM products'
    res=cursor.fetchone()
    #Checking if the quantity of the 1st product is entered and calculating price, showing it on window  and adding to database 
    if(len(name1.get()) != 0):
        i=res[0]
        qty=int(name1.get())
        total=qty*int(i[2])
        tk.Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
        
    #Checking if the quantity of the 2nd product is entered and calculating price, showing it on window  and adding to database 
    if(len(name2.get()) != 0):
        i=res[1]
        qty=int(name2.get())
        total=qty*int(i[2])
        tk.Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
    
    #Checking if the quantity of the 3rd product is entered and calculating price, showing it on window  and adding to database 
    if(len(name3.get()) != 0):
        i=res[2]
        qty=int(name3.get())
        total=qty*int(i[2])
        tk.Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
    #showing total of the bill
    tk.Label(labelFrame, text = "------------------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=y)
    y+=0.1
    tk.Label(labelFrame,text="\t\t\t\t\t\t\t\t"+str(totalBill) ,fg='black').place(relx=0.07,rely=y)
    
    Quit = tk.Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
#Function to take the inputs form the user to generate bill    
def newCust():    
    global wn,name1,name2,name3,date,custName
    #Creating a window
    wn = tk.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='lavenderblush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = tk.Frame(wn,bg="lavenderblush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = tk.Label(headingFrame1, text="New Customer", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lable1 = tk.Label(wn,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, )
        
    #Getting date
    date = tk.Entry(wn)
    date.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    lable2 = tk.Label(wn,text="Customer Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.4, )
      
    #Getting customer name
    custName = tk.Entry(wn)
    custName.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    labelFrame = tk.Frame(wn)
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.4)
    
    y = 0.3
    tk.Label(labelFrame, text="Please enter the quantity of the products you want to buy",font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    
    tk.Label(labelFrame, text="%-50s%-50s%-30s"%('Product','Price','Quantity'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    
    #Connecting to the database
    db=msql.connect(user="python",passwd="python",host="localhost",database='Shop') 
    cursor=db.cursor()
    query = 'SELECT * FROM products'

    cursor.execute(query)
    res = cursor.fetchall() 
    print(res)
    c=1
    
    #Showing all the products and creating entries to take the input of the quantity
    i=res[0]
    tk.Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name1 = tk.Entry(labelFrame)
    name1.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[1]
    tk.Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name2 = tk.Entry(labelFrame)
    name2.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[2]
    tk.Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name3 = tk.Entry(labelFrame)
    name3.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
     #Button to generate bill
    Btn= tk.Button(wn,text="Generate Bill",bg='#d1ccc0', fg='black',command=bill)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = tk.Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)

    wn.mainloop()

#Creating the GUI
#Creating the main window
wn = tk.Tk() 
wn.title("PythonGeeks Shop Management System")
wn.configure(bg='honeydew2')
wn.minsize(width=500,height=500)
wn.geometry("700x600")

headingFrame1 = tk.Frame(wn,bg="snow3",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = tk.Label(headingFrame1, text="Welcome to PythonGeeks \n Shop Management System", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Button to add a new product
btn1 = tk.Button(wn,text="Add a Product",bg='LightBlue1', fg='black', width=20,height=2, command=addProd)
btn1['font'] = tk.font.Font( size=12)
btn1.place(x=270,y=175)

#Button to delete a product
btn2 = tk.Button(wn,text="Delete a Product",bg='misty rose', fg='black',width=20,height=2,command=delProd)
btn2['font'] = tk.font.Font( size=12)
btn2.place(x=270,y=255)

#Button to view all products
btn3 = tk.Button(wn,text="View Products",bg='old lace', fg='black',width=20,height=2,command=viewProds)
btn3['font'] = tk.font.Font( size=12)
btn3.place(x=270,y=335)

#Button to add a new sale and generate bill
btn4 = tk.Button(wn,text="New Customer",bg='lavenderblush2', fg='black', width=20,height=2,command = newCust)
btn4['font'] = tk.font.Font( size=12)
btn4.place(x=270,y=415)


wn.mainloop()

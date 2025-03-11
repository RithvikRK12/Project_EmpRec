import tkinter as Tk
from tkinter import *
from PIL import ImageTk
from tkinter import filedialog
from tkinter import messagebox
import time
import ttkthemes
from tkinter import ttk
import pymysql
import pandas

# Functions

def iexit():
    result = messagebox.askyesno('CONFIRM', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_employee():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = EmpTable.get_children()
    new_list = []
    for index in indexing:
        content = EmpTable.item(index)
        datalist = content['values']
        new_list.append(datalist)
    table = pandas.DataFrame(new_list,columns = ['Id','Name','Phone','Email','Adress','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url, index = False)
    messagebox.showinfo('SUCCESS', 'Data has been exported')

    

def update_employee():

    def update_data():

        query = 'update employee set name=%s,mobile=%s,email=%s,adress=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query, (Nameentry.get(),Phoneentry.get(), Emailentry.get(), Adressentry.get(), Genderentry.get(), dobentry.get(),date, CurrentTime, identry.get()))
        con.commit()
        messagebox.showinfo('SUCCESS', 'Id Modified Succcessfully', parent = update_window)
        update_window.destroy()
        show_employee()

    update_window = Toplevel()
    update_window.title('Update Employee')
    update_window.grab_set()
    update_window.resizable(0,0)
    idlabel = Label(update_window, text = 'Id', font = ('times new roman',20, 'bold'))
    idlabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W)
    identry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    identry.grid(row =0, column = 1, padx = 15, pady = 20)

    Namelabel = Label(update_window, text = 'Name', font = ('times new roman',20, 'bold'))
    Namelabel.grid(row = 1, column = 0, padx = 30, pady = 15, sticky = W)
    Nameentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    Nameentry.grid(row =1, column = 1, padx = 15, pady = 20)

    Phonelabel = Label(update_window, text = 'Phone', font = ('times new roman',20, 'bold'))
    Phonelabel.grid(row = 2, column = 0, padx = 30, pady = 15, sticky = W)
    Phoneentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    Phoneentry.grid(row =2, column = 1, padx = 15, pady = 20)

    Emaillabel = Label(update_window, text = 'Email', font = ('times new roman',20, 'bold'))
    Emaillabel.grid(row = 3, column = 0, padx = 30, pady = 15, sticky = W)
    Emailentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    Emailentry.grid(row =3, column = 1, padx = 15, pady = 20)

    Adresslabel = Label(update_window, text = 'Adress', font = ('times new roman',20, 'bold'))
    Adresslabel.grid(row = 4, column = 0, padx = 30, pady = 15, sticky = W)
    Adressentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    Adressentry.grid(row = 4, column = 1, padx = 15, pady = 20)

    Genderlabel = Label(update_window, text = 'Gender', font = ('times new roman',20, 'bold'))
    Genderlabel.grid(row = 5, column = 0, padx = 30, pady = 15, sticky = W)
    Genderentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    Genderentry.grid(row =5, column = 1, padx = 15, pady = 20)

    doblabel = Label(update_window, text = 'D.O.B.', font = ('times new roman',20, 'bold'))
    doblabel.grid(row = 6, column = 0, padx = 30, pady = 15, sticky = W)
    dobentry = Entry(update_window, font = ('times new roman', 15, 'bold'), width = 24)
    dobentry.grid(row =6, column = 1, padx = 15, pady = 20)

    update_emp_button = ttk.Button(update_window, text = 'UPDATE', command = update_data)
    update_emp_button.grid(row = 7, columnspan=2, pady = 15)

    indexing = EmpTable.focus()
    content = EmpTable.item(indexing)
    listdata = content['values']
    identry.insert(0,listdata[0])
    Nameentry.insert(0,listdata[1])
    Phoneentry.insert(0,listdata[2])
    Emailentry.insert(0,listdata[3])
    Adressentry.insert(0,listdata[4])
    Genderentry.insert(0,listdata[5])
    dobentry.insert(0,listdata[6])

def show_employee():
    query = 'select * from employee'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    EmpTable.delete(*EmpTable.get_children())
    for data in fetched_data:
        EmpTable.insert('', END, values = data)



def delete_employee():
    indexing = EmpTable.focus()
    print(indexing)
    content = EmpTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from employee where id=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('SUCCESS', 'Employee record deleted')
    query = 'select * from employee'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    EmpTable.delete(*EmpTable.get_children())
    for data in fetched_data:
        EmpTable.insert('', END, values = data)

def search_employee():
    def search_data():
        
        query = 'select * from employee where id=%s or name=%s or email=%s or mobile=%s or adress=%s or gender=%s or dob=%s'
        mycursor.execute(query,(identry.get(),Nameentry.get(),Emailentry.get(), Phoneentry.get(), Adressentry.get(), Genderentry.get(), dobentry.get()))
        EmpTable.delete(*EmpTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            EmpTable.insert('',END, values = data)


    search_window = Toplevel()
    search_window.title('Search Employee')
    search_window.grab_set()
    search_window.resizable(0,0)
    idlabel = Label(search_window, text = 'Id', font = ('times new roman',20, 'bold'))
    idlabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W)
    identry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    identry.grid(row =0, column = 1, padx = 15, pady = 20)

    Namelabel = Label(search_window, text = 'Name', font = ('times new roman',20, 'bold'))
    Namelabel.grid(row = 1, column = 0, padx = 30, pady = 15, sticky = W)
    Nameentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    Nameentry.grid(row =1, column = 1, padx = 15, pady = 20)

    Phonelabel = Label(search_window, text = 'Phone', font = ('times new roman',20, 'bold'))
    Phonelabel.grid(row = 2, column = 0, padx = 30, pady = 15, sticky = W)
    Phoneentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    Phoneentry.grid(row =2, column = 1, padx = 15, pady = 20)

    Emaillabel = Label(search_window, text = 'Email', font = ('times new roman',20, 'bold'))
    Emaillabel.grid(row = 3, column = 0, padx = 30, pady = 15, sticky = W)
    Emailentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    Emailentry.grid(row =3, column = 1, padx = 15, pady = 20)

    Adresslabel = Label(search_window, text = 'Adress', font = ('times new roman',20, 'bold'))
    Adresslabel.grid(row = 4, column = 0, padx = 30, pady = 15, sticky = W)
    Adressentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    Adressentry.grid(row = 4, column = 1, padx = 15, pady = 20)

    Genderlabel = Label(search_window, text = 'Gender', font = ('times new roman',20, 'bold'))
    Genderlabel.grid(row = 5, column = 0, padx = 30, pady = 15, sticky = W)
    Genderentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    Genderentry.grid(row =5, column = 1, padx = 15, pady = 20)

    doblabel = Label(search_window, text = 'D.O.B.', font = ('times new roman',20, 'bold'))
    doblabel.grid(row = 6, column = 0, padx = 30, pady = 15, sticky = W)
    dobentry = Entry(search_window, font = ('times new roman', 15, 'bold'), width = 24)
    dobentry.grid(row =6, column = 1, padx = 15, pady = 20)

    Search_emp_button = ttk.Button(search_window, text = 'SEARCH EMPLOYEE', command = search_data)
    Search_emp_button.grid(row = 7, columnspan=2, pady = 15)


def add_employee():
    def add_data():
        if identry.get()==''or Nameentry.get()=='' or Phoneentry.get()=='' or Emailentry.get()=='' or Adressentry.get()=='' or Genderentry.get()=='' or dobentry.get()=='':
            messagebox.showerror('ERROR', 'Fields cannot be empty!', parent = add_window)
        else:
            try:
                query = 'insert into employee values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                mycursor.execute(query, (identry.get(), Nameentry.get(), Phoneentry.get(), Emailentry.get(), Adressentry.get(), Genderentry.get(), dobentry.get(), date, CurrentTime))
                con.commit()
                result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?', parent = add_window)
                if result:
                    identry.delete(0, END)
                    Nameentry.delete(0, END)
                    Phoneentry.delete(0, END)
                    Emailentry.delete(0, END)
                    Adressentry.delete(0, END)
                    Genderentry.delete(0, END)
                    dobentry.delete(0, END)

                else:
                    pass
            except:
                messagebox.showerror('ERROR', 'Id cannot be repeated', parent = add_window)

            query = 'select *from employee'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            EmpTable.delete(*EmpTable.get_children())
            for data in fetched_data:
                EmpTable.insert('', END, values = data)

    add_window = Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    idlabel = Label(add_window, text = 'Id', font = ('times new roman',20, 'bold'))
    idlabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W)
    identry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    identry.grid(row =0, column = 1, padx = 15, pady = 20)

    Namelabel = Label(add_window, text = 'Name', font = ('times new roman',20, 'bold'))
    Namelabel.grid(row = 1, column = 0, padx = 30, pady = 15, sticky = W)
    Nameentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    Nameentry.grid(row =1, column = 1, padx = 15, pady = 20)

    Phonelabel = Label(add_window, text = 'Phone', font = ('times new roman',20, 'bold'))
    Phonelabel.grid(row = 2, column = 0, padx = 30, pady = 15, sticky = W)
    Phoneentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    Phoneentry.grid(row =2, column = 1, padx = 15, pady = 20)

    Emaillabel = Label(add_window, text = 'Email', font = ('times new roman',20, 'bold'))
    Emaillabel.grid(row = 3, column = 0, padx = 30, pady = 15, sticky = W)
    Emailentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    Emailentry.grid(row =3, column = 1, padx = 15, pady = 20)

    Adresslabel = Label(add_window, text = 'Adress', font = ('times new roman',20, 'bold'))
    Adresslabel.grid(row = 4, column = 0, padx = 30, pady = 15, sticky = W)
    Adressentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    Adressentry.grid(row = 4, column = 1, padx = 15, pady = 20)

    Genderlabel = Label(add_window, text = 'Gender', font = ('times new roman',20, 'bold'))
    Genderlabel.grid(row = 5, column = 0, padx = 30, pady = 15, sticky = W)
    Genderentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    Genderentry.grid(row =5, column = 1, padx = 15, pady = 20)

    doblabel = Label(add_window, text = 'D.O.B.', font = ('times new roman',20, 'bold'))
    doblabel.grid(row = 6, column = 0, padx = 30, pady = 15, sticky = W)
    dobentry = Entry(add_window, font = ('times new roman', 15, 'bold'), width = 24)
    dobentry.grid(row =6, column = 1, padx = 15, pady = 20)

    Add_emp_button = ttk.Button(add_window, text = 'ADD EMPLOYEE', command = add_data)
    Add_emp_button.grid(row = 7, columnspan=2, pady = 15)

def clock():
    global date, CurrentTime
    date = time.strftime('%d/%m/%Y')
    CurrentTime = time.strftime('%H:%M:%S')
    DateTimeLabel.config(text = f'   Date: {date}\nTime: {CurrentTime}')
    DateTimeLabel.after(1000,clock)  # To call after every 1 second

count = 0
text = ''
def Slider():
    global text,count  # to update valuse inside and outside function
    if count==len(str):
        count = 0
        text = ''
    text = text + str[count]
    TopTitle.config(text = text)
    count = count + 1
    TopTitle.after(100,Slider)

def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host=hostentrylabel.get(), user=userentrylabel.get(), password = passwordentrylabel.get())
            mycursor = con.cursor()
            
        except:
            messagebox.showerror('ERROR', 'Invalid details', parent = connectwindow)
            return
        try:
            query = 'create database employeerecords'
            mycursor.execute(query)
            query = 'use employeerecords'
            mycursor.execute(query)
            query = 'create table Employee(Id int not null primary key, Name varchar(30), Mobile varchar(30), Email varchar(30), Adress varchar(100), Gender varchar(20), DOB varchar(20), Date varchar(50), Time varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use employeerecords'    #if table already exists
            mycursor.execute(query)
        messagebox.showinfo('SUCCESS', 'Database Connection eshtabilished', parent = connectwindow)
        connectwindow.destroy()
        AddEmpButton.config(state = NORMAL)
        SearchEmpButton.config(state = NORMAL)
        DeleteEmpButton.config(state = NORMAL)
        UpdateEmpButton.config(state = NORMAL)
        ShowEmpButton.config(state = NORMAL)
        ExportEmpButton.config(state = NORMAL)
        

    connectwindow = Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnamelabel = Label(connectwindow, text = 'Host Name', font = ('arial',18,'bold'))
    hostnamelabel.grid(row = 0, column = 0, padx = 20)

    hostentrylabel = Entry(connectwindow, font = ('times new roman', 13, 'bold'),bd = 2)
    hostentrylabel.grid(row = 0, column = 1, padx = 40, pady = 20)

    usernamelabel = Label(connectwindow, text = 'User Name', font = ('arial',18,'bold'))
    usernamelabel.grid(row = 1, column = 0, padx = 20)

    userentrylabel = Entry(connectwindow, font = ('times new roman', 13, 'bold'),bd = 2)
    userentrylabel.grid(row = 1, column = 1, padx = 40, pady = 20)

    passwordlabel = Label(connectwindow, text = 'Password', font = ('arial',18,'bold'))
    passwordlabel.grid(row = 2, column = 0, padx = 20)

    passwordentrylabel = Entry(connectwindow, font = ('times new roman', 13, 'bold'),bd = 2)
    passwordentrylabel.grid(row = 2, column = 1, padx = 40, pady = 20)

    connectdata = Button(connectwindow, text = 'CONNECT', font = ('arial', 15, 'bold'), bg = 'skyblue', fg = 'white', command = connect)
    connectdata.grid(row = 3, column = 1)


# GUI
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('radiance')


root.geometry("1280x800+0+0")
root.title('Employee Records')
root.resizable(False,False) 

DateTimeLabel = Label(root, text = 'hello', font = ('aldhabi', 14, 'bold'))
DateTimeLabel.place(x = 5, y= 5)
clock()

str = 'Employee Records Management System'
TopTitle = Label(root, text = str, font = ('aldhabi', 20, 'italic bold'), width = 30)
TopTitle.place(x = 400, y = 0)
Slider()

ConnectButton = ttk.Button(root, text = 'Connect Database', command=connect_database)
ConnectButton.place(x = 1100, y = 10)

LeftFrame = Frame(root)
LeftFrame.place(x = 80, y = 80, width = 300, height = 700)

AddEmpButton = ttk.Button(LeftFrame, text = 'Add Employee', state = DISABLED, command = add_employee)
AddEmpButton.grid(row = 1, column = 0, pady = 25)

SearchEmpButton = ttk.Button(LeftFrame, text = 'Search Employee', state = DISABLED, command=search_employee)
SearchEmpButton.grid(row = 2, column = 0, pady = 25)

DeleteEmpButton = ttk.Button(LeftFrame, text = 'Delete Employee', state = DISABLED, command = delete_employee)
DeleteEmpButton.grid(row = 3, column = 0, pady = 25)

UpdateEmpButton = ttk.Button(LeftFrame, text = 'Update Employee', state = DISABLED, command = update_employee)
UpdateEmpButton.grid(row = 4, column = 0, pady = 25)

ShowEmpButton = ttk.Button(LeftFrame, text = 'Show Employee', state = DISABLED, command = show_employee)
ShowEmpButton.grid(row = 5, column = 0, pady = 25)

ExportEmpButton = ttk.Button(LeftFrame, text = 'Export Employee', state = DISABLED, command = export_employee)
ExportEmpButton.grid(row = 6, column = 0, pady = 25)

ExitButton = ttk.Button(LeftFrame, text = 'Exit', command = iexit)
ExitButton.grid(row = 7, column = 0, pady = 80)

RightFrame = Frame(root)
RightFrame.place(x = 325, y = 100, width = 875, height = 650)

Scrollbarx = Scrollbar(RightFrame, orient=HORIZONTAL)
Scrollbary = Scrollbar(RightFrame, orient=VERTICAL)

EmpTable = ttk.Treeview(RightFrame, column = ('Id', 'Name', 'Mobile No', 'Email', 'Adress', 'Gender', 'D.O.B.','Added Date', 'Added Time'),
                        xscrollcommand = Scrollbarx.set, yscrollcommand = Scrollbary.set)

Scrollbarx.config(command = EmpTable.xview)
Scrollbary.config(command = EmpTable.yview)


EmpTable.heading('Id', text = 'Id')
EmpTable.heading('Name', text = 'Name')
EmpTable.heading('Mobile No', text = 'Mobile No')
EmpTable.heading('Email', text = 'Email')
EmpTable.heading('Adress', text = 'Adress')
EmpTable.heading('Gender', text = 'Gender')
EmpTable.heading('D.O.B.', text = 'D.O.B.')
EmpTable.heading('Added Date', text = 'Added Date')
EmpTable.heading('Added Time', text = 'Added Time')


EmpTable.config(show = 'headings')

Scrollbarx.pack(side = BOTTOM, fill = X)
Scrollbary.pack(side = RIGHT, fill = Y)

EmpTable.pack(fill = BOTH, expand = 1)

root.mainloop()


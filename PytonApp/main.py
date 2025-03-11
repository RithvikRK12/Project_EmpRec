import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk                                                       # for jpg images

window = Tk()                                                                 # assigning object to the Tk class

def Login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('ERROR!', 'Fields cannot be empty') 
    elif UsernameEntry.get()=='Rithvik' and PasswordEntry.get()=='12345':
        messagebox.showinfo('SUCCESS', 'Welcome')
        window.destroy()
        import ms                                                             # database functionalites
        

    else:
        messagebox.showerror('ERROR!', 'Username Or Password is incorrect')


window.geometry('1280x800+0+0')                                                   # window l x b

window.title('Login System for Employee Records')

window.resizable(False,False)                                                 # disable maximize 

bkImage = ImageTk.PhotoImage(file = 'bg.jpg')
bgLabel = Label(window, image = bkImage)
bgLabel.place(x = 0, y = 0)                                                   # Placing image on window

LoginFrame = Frame(window, bg = 'White')
LoginFrame.place(x = 465, y = 250)                                            # Placing Frame inside window

LogoImage = PhotoImage(file = 'logo.png')

LogoLabel = Label(LoginFrame, image = LogoImage, bg = 'white' )                             # Placing Labels inside the Login frame
LogoLabel.grid(row = 0, column = 0, columnspan = 2, pady = 10)                           # logolabel will take 2 columnspaces

UsernameImage = PhotoImage(file = 'man.png')

UsernameLabel = Label(LoginFrame, image = UsernameImage, text = 'Username', compound = LEFT,
                       font = ('abadi', 18, 'bold'), bg = 'white', padx = 10)
UsernameLabel.grid(row = 1, column = 0)

UsernameEntry = Entry(LoginFrame, font = ('abadi', 15), bd = 2)
UsernameEntry.grid(row = 1, column = 1, pady = 10)

PasswordImage = PhotoImage(file = 'lock.png')

PasswordLabel = Label(LoginFrame, image = PasswordImage, text = 'Password', compound = LEFT,
                       font = ('abadi', 18, 'bold'), bg = 'white', padx = 10)
PasswordLabel.grid(row = 2, column = 0)

PasswordEntry = Entry(LoginFrame, font = ('abadi', 15), bd = 2)
PasswordEntry.grid(row = 2, column = 1, pady = 10)

LoginButton = Button(LoginFrame, text = 'Login', font = ('abadi', 18), width = 10, fg = 'white', bg = 'cornflowerblue',
                     activebackground = 'cornflowerblue', activeforeground = 'white', cursor = 'hand2', command = Login)
LoginButton.grid(row = 3, column = 1)

window.mainloop()                                                             # Window visible continously

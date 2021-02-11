from tkinter import *
import os
from PIL import ImageTk, Image

#create main screen
master = Tk()
master.title("Banking app")

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()

    #store information and make sure no duplicates are stored
    all_accounts = os.listdir()

    if name =="" or age =="" or gender=="" or password=="":
        notif.config(fg='red',text='All fields required *')
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg='red', text="Account name already exists")
            return
    else:
        new_file = open(name,"w")
        new_file.write(name + "\n")
        new_file.write(name + "\n")
        new_file.write(name + "\n")
        new_file.write(name + "\n")
        new_file.close()
        notif.config(fg='green', text='Account has been created')


#functions
def register():
    #vars make --->> available to whole program with global
    global  temp_name
    global  temp_gender
    global  temp_age
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password =StringVar()

    #register screen
    register_screen = Toplevel(master)
    register_screen.title("Register")
    #Labels
    Label(register_screen, text="Please enter your details below to register", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=("Calibri",12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=("Calibri",12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password",font=("Calibiri",12)).grid(row=4,sticky=W)
    notif = Label(register_screen, text="Register",font=("Calibri",12))
    notif.grid(row=6,sticky=N,pady=10)
    #enteries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    #the show = * is to hide the entry
    Entry(register_screen,textvariable=temp_password,show="*").grid(row=4,column=0)

    #Buttons
    Button(register_screen,text="Register", command=finish_reg,font=("Calibri", 12)).grid(row=5,sticky=N,pady=10)
    print("This is a login page")

def login():
    print("This is a login page")




#Image import
img = Image.open('bank.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)


#Labels
Label(master, text = "Custom Banking Beta", font=("Calibri", 14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "the most secure bank you've probably", font=("Calibri", 12)).grid(row=1,sticky=N,pady=10)
Label(master, image=img).grid(row=2, sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=("Calibri",12),width=20,command=register).grid(row=3,sticky=N)
Button(master, text="Login", font=("Calibri",12),width=20,command=login).grid(row=4,sticky=N)

master.mainloop()

from tkinter import *
import random

root = Tk()
root.title("CSCI 401 Project")
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#=====================================METHODS===================================
def Random():
   # alphabet = "abcdefghijklmnopqrstuvwxyz"
   # length = 8
    new_password = ""

    PASSWORD.set(new_password);
#====================================VARIABLES==================================
PASSWORD = StringVar()
 
#====================================FRAME======================================
Top = Frame(root, width=width)
Top.pack(side=TOP)
Form = Frame(root, width=width)
Form.pack(side=TOP)
 
#====================================LABEL WIDGET===============================
lbl_title = Label(Top, width=width, font=('arial', 16), text="Machine Learning Project", bd=1, relief=SOLID)
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('arial', 18), text="Password :", bd=10)
lbl_password.grid(row=0, pady=15)
#====================================ENTRY WIDGET===============================
password = Entry(Form, textvariable=PASSWORD, font=(18), width=16)
password.grid(row=0, column=1)
#====================================BUTTON WIDGET==============================
btn_generate = Button(Form, text="Check", width=20, command=Random)
btn_generate.grid(row=1, columnspan=2)

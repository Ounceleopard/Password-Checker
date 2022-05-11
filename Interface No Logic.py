from tkinter import *
import hashlib
import random
import requests

root = Tk()

root.title("EASY PASS")
width = 500
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

# METHODS
def checkPassword():
    password_input = password.get()
    sha_password = hashlib.sha1(password_input.encode()).hexdigest()
    sha_prefix = sha_password[0:5]
    sha_post = sha_password[5:].upper()
    # Key Is Valid Until JUNE 11 2022: For New key https://haveibeenpwned.com/API/Key
    API_KEY = "01d039b307494dc68509e0e6a358699c"
    response_url = "https://api.pwnedpasswords.com/range/" + sha_prefix

    response = requests.request("GET", response_url)

    #Split the response text based on \r\n
    password_dict = {}
    password_list = response.text.split("\r\n")
    for pwd in password_list:
        hash = pwd.split(":")
        password_dict[hash[0]] = hash[1]
    # Output to program display
    if sha_post in password_dict.keys():
       lbl_title = Label(Bottom, width=width, font=('arial', 16), fg = 'green',text='Password has been breached {0}'.format(password_dict[sha_post]), bd=1, relief='flat')
       lbl_title.pack(fill=X)
    else:
        lbl_title = Label(Bottom, width=width, font=('arial', 16), fg = 'red',text="No breaches detected!", bd=1, relief='flat')
        lbl_title.pack(fill=X)
        
# VARIABLES
PASSWORD = StringVar()

# FRAME
Top = Frame(root, width=width)
Top.pack(side=TOP)
Form = Frame(root, width=width)
Form.pack(side=TOP)

#Output Display For API Result 
Bottom = Frame(root, width=width)
Bottom.pack(side=TOP)

# LABEL WIDGET
lbl_title = Label(Top, width=width, font=('arial', 20), text="Machine Learning Project", bd=1, relief='flat')
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('arial', 14), text="Enter Password ", bd=11)
lbl_password.grid(row=0, pady=17)

# ENTRY WIDGET
password = Entry(Form, textvariable=PASSWORD, font=(18), width=16)
password.grid(row=0, column=1)

# BUTTON WIDGET
btn_generate = Button(Form, font=('arial',11),text="Check", width=20, command= checkPassword)
btn_generate.grid(row=3, columnspan=2)

root.mainloop()
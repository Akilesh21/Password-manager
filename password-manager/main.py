from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox
import random 
import json

from click import command

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def Generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    num = ["0","1","2","3","4","5","6","7","8","9"]
    nr_letters =random.randint(8,10)
    nr_symbols =random.randint(2,4)
    nr_numbers =random.randint(2,4)
    
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(num) for _ in range(random.randint(2,4))]
    
    password_list = password_letters + password_symbols + password_numbers
     
    random.shuffle(password_list)
    generate_password = "".join(password_list)
    password_entry.insert(0,generate_password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }

    }

    if len(website) ==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail:{email}"
                                                     f"\n Password:{password} \nIS it ok to save?" )
        if is_ok:
            try:
                with open("tkinter_gui/password-manager/data.json","r") as data_file:
                    #Reading the old data
                    data=json.load(data_file) #---> load is used to read the data in json file
                    #Updating the old into new data
            except FileNotFoundError:
                    with open("tkinter_gui/password-manager/data.json","w") as data_file:
                        json.dump(new_data,data_file,indent=4)
            else:    
                    data.update(new_data) # ----> update is used to update the json file with new data
                    #Saving the new data            
                    with open("tkinter_gui/password-manager/data.json","w") as data_file:
                        json.dump(data,data_file,indent=4) #--->dump is used to write the data in json file
            finally:            
                    website_entry.delete(0,END)
                    email_entry.delete(0,END)
                    password_entry.delete(0,END)
        else:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)        
# -------------------FIND PASSWORD ----------------------------------#
def find_password():
    website = website_entry.get()
    try:
        with open("tkinter_gui/password-manager/data.json") as data_file:
            data =json.load(data_file)
    except FileNotFoundError:     
        messagebox.showinfo(title=website,message="NO Data file found ")      
    else:    
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:    
            messagebox.showinfo(title="Error",message=f"NO Details for {website} exits")   
         


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="tkinter_gui/password-manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


#labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row = 3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1)
password_entry= Entry(width=35)
password_entry.grid(row=3,column=1)

#Buttons
generate_password_button = Button(text="Generate Password",command=Generate_password)

generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button  =Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)
window.mainloop()
from email import message
from tkinter import * 
from tkinter import messagebox
import random
import pyperclip 
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for char in range(nr_letters)] 
    
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    Password_entry.insert(END, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def addition():
    website = website_entry.get()
    user = user_entry.get()
    Password = Password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": Password,
        }
    }
   
    gun =[website,user,Password]

    if len(website) == 0 or len(Password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}\n"
                                                            f"\nPassword: {Password} \nIs it okay to save ?")
        if is_ok :
            try:                                       
             with open("password-manager-start//data.json","r") as file:
                # json.dump(new_data, file, indent=4)
                #Reading old data
                data = json.load(file)
            except FileNotFoundError:
                with open("password-manager-start//data.json","w") as file:
                    json.dump(new_data, file, indent= 4)
                #updating old data with new data

            else:
                data.update(new_data)
            
                with open("password-manager-start//data.json","w") as file:
                #saving updated data
                    json.dump(data, file, indent= 4)
                # print(data)
                # file.write(str(all) + "\n")
            finally:
                website_entry.delete(0,END)
            # user_entry.delete(0,END)
                Password_entry.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #
def find_password () :
    website = website_entry.get()
    try:
        with open("password-manager-start//data.json","r") as file:
                data = json.load(file)
    except:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Message", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message= f"No details for The {website} exists")
    
    

    



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )



canvas = Canvas(width=240, height=240)
tomato_img = PhotoImage(file="password-manager-start//logo.png")
canvas.create_image(120, 100, image=tomato_img)
canvas.grid(column=0,row=0)


website_label = Label(text="Website :")
website_label.grid(column=0, row=1)


user_label = Label(text="Email/Username : ")
user_label.grid(column=0, row=2)



Password_label = Label(text="Password :")
Password_label.grid(column=0, row=3)


website_entry = Entry(width = 35)
# website_entry.insert(END, string="email.nsk.ai@gmail.com")
website_entry.focus()
website_entry.grid(column=1, row=1,columnspan=2)




user_entry = Entry(width = 35)
user_entry.insert(END, string="ifeanyi@nskai.com")
# user_entry.focus()
user_entry.grid(column=1, row=2,columnspan=2)


Password_entry = Entry(width = 35)
# Password_entry.insert(END, string="Please insert or generate a Password here ")
# Password_entry.focus()
Password_entry.grid(column=1, row=3,columnspan=2)


Generate_button = Button(text="Generate Password",width = 20, command=generate_Password)
Generate_button.grid(column=1, row=5, columnspan=2)

Add_button = Button(text="Add",width = 20,command=addition)
Add_button.grid(column=1, row=6, columnspan=2)


Search_button = Button(text="Search",width = 20,command=find_password)
Search_button.grid(column=1, row=7, columnspan=2)




website = website_entry.get()
tem = user_entry.get()
lod = Password_entry.get()
all = list(website + tem + lod)


























window.mainloop()
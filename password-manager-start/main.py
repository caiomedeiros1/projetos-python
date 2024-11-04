from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- FIND PASSWORD ------------------------------------ #

def find_password():
    website = website_input.get().capitalize()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email/Username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_random_password():
    password_input.delete(0, END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 12)
    nr_symbols = random.randint(2, 6)
    nr_numbers = random.randint(2, 6)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    final_password = "".join(password_list)
    password_input.insert(0, final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get().capitalize()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Make sure you've filled in all the fields.")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                #Writing file for the first time
                json.dump(new_data, data_file, indent=4)

        else:  
            if website in data:
                yes_or_no = messagebox.askyesno(title="Website already saved", message="This website has already been saved.\n Do you want to replace information?")     
                if yes_or_no:
                    #Updating the data
                    data.update(new_data)
                    with open("data.json", mode="w") as data_file:
                        #Saving updated data
                        json.dump(data, data_file, indent=4)
            else:
                #Updating the data
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

#Labels
website = Label(text="Website: ")
website.grid(row=1, column=0)
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)
password = Label(text="Password: ")
password.grid(row=3, column=0)

#Entries
website_input = Entry(width=34)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=52)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=34)
password_input.grid(row=3, column=1)

#Buttons
search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)
generate_password = Button(text="Generate Password", command=generate_random_password, width=14)
generate_password.grid(row=3, column=2)
add = Button(text="Add", width=28, command=save_password)
add.grid(row=4, column=1)

window.mainloop()
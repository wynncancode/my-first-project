from tkinter import *
from tkinter import messagebox
import random
#You will need to install the package pyperclip if you haven't done so.
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    data_website = input_website.get()
    data_email = input_email.get()
    data_password = input_password.get()

    if len(data_email) == 0 or len(data_password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=data_website, message=f"These are the details entered: \nEmail: {data_email}"
                                                           f"\nPassword: {data_password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode = "a") as data_file:
                data_file.write(f"{data_website} | {data_email} | {data_password}\n")

            input_website.delete(0,END)
            input_email.delete(0, END)
            input_email.insert(0,"abc@email.com")
            input_password.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas (width=200, height=200)
keylock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=keylock_img)
canvas.grid(column=1, row=0)

#Label
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

#Entry
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, "abc@email.com")

input_password = Entry(width=20)
input_password.grid(column=1, row=3)

#Button
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=1, row=4, columnspan=2)



window.mainloop()
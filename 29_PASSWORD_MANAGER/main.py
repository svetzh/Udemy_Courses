from tkinter import *
import pyperclip
from tkinter import messagebox
from random import randint, choice, shuffle


GREEN = "#D0E7D2"
GREEN_DARK = "#B0D9B1"

# ---------------------------- PASSWORD HIDING ------------------------------- #
def toggle_pass_visibility():
    if show_passwd.get():
        pass_entry.config(show="")
    else:
        pass_entry.config(show="*")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lst = ([choice(letters) for _ in range(randint(8, 10))]
                    + [choice(symbols) for _ in range(randint(2, 4))]
                    + [choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_lst)
    password = "".join(password_lst)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    mail_user = email_entry.get()
    password_entr = pass_entry.get()

    if len(website) == 0 or len(password_entr) == 0:
        messagebox.showinfo(title="Ooops", message='Fill in all empty fields!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details inserted: \nEmail/User: {mail_user}: "
                                                  f"\nPass: {password_entr} \nSAVE?")
        if is_ok:
            with open("data_saver.txt", mode="a") as file:
                file.write(f"{website} | {mail_user} | {password_entr}\n")
                web_entry.delete(0, END)
                # email_entry.delete(0, END)
                pass_entry.delete(0, END)
                show_passwd.set(False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pass Manager")
window.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
pass_img = PhotoImage(file='pass-pic.png')
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Label Website
website_labels = Label(text="Website:", bg=GREEN, font=("Consolas", 12), highlightthickness=0)
website_labels.grid(row=1, column=0, sticky="e")

emai_labels = Label(text="Email/Username:", bg=GREEN, font=("Consolas", 12))
emai_labels.grid(row=2, column=0, sticky="e")

password_labels = Label(text="Password:", bg=GREEN, font=("Consolas", 12))
password_labels.grid(row=3, column=0, sticky="e")

# Entries
web_entry = Entry(width=50, bg=GREEN, font=("Consolas", 10))
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")
web_entry.focus()

email_entry = Entry(width=50, bg=GREEN, font=("Consolas", 10))
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "mrsvetoslav@gmail.com")

pass_entry = Entry(width=20, bg=GREEN, font=("Consolas", 10), show="*")
pass_entry.grid(row=3, column=1, sticky="w")  # sticky="w"

# Buttons
generate_pass = Button(text="Generate Password", bg=GREEN_DARK, font=("Consolas", 11), command=generate_password)
generate_pass.grid(row=3, column=2, sticky="e")

add_button = Button(text="Add", width=36, bg=GREEN_DARK, font=("Consolas", 11), command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

# Check Button
show_passwd = BooleanVar()
show_pass_check = Checkbutton(text="Show Pass", variable=show_passwd, bg=GREEN,
                              font=("Consolas", 10), command=toggle_pass_visibility)
show_pass_check.grid(row=3, column=1, sticky="e")

window.mainloop()
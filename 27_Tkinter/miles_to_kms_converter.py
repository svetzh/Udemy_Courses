from tkinter import *


MILE_KMS = 1.609344
KMS_MILS = 0.621371

def set_to_kms():
    unit_var.set("Km")
    lbl2.config(text="Miles")
    lbl3.config(text="Km")

def set_to_miles():
    unit_var.set("Miles")
    lbl2.config(text="Km")
    lbl3.config(text="Miles")

def calculate():
    value = miles_input.get()
    try:
        value = float(value)
        if unit_var.get() == "Km":
            result = value * MILE_KMS
            lbl4.config(text=f"{result:2f}")
        else:
            result = value * KMS_MILS
            lbl4.config(text=f"{result:2f}")
    except ValueError:
        lbl4.config(text="Invalid input!")

window = Tk()
window.title("Mils/Kms Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

# Label
lbl = Label(text="is equal to:", font=("Consolas", 15))
lbl.grid(row=1, column=0)
lbl.config(padx=10, pady=10)

lbl2 = Label(text="Miles", font=("Consolas", 15))
lbl2.grid(row=0, column=2)
lbl2.config(padx=10, pady=10)

lbl3 = Label(text="Km", font=("Consolas", 15))
lbl3.grid(row=1, column=2)
lbl3.config(padx=10, pady=10)

lbl4 = Label(font=("Consolas", 15))
lbl4.grid(row=1, column=1)
lbl4.config(padx=10, pady=10)

# Radio Button
unit_var = StringVar()
unit_var.set("Km")
km_button = Radiobutton(window, text="Km", variable=unit_var, value="Km", command=set_to_kms)
km_button.grid(row=2, column=2)

ml_button = Radiobutton(window, text="Miles", variable=unit_var, value="Miles", command=set_to_miles)
ml_button.grid(row=3, column=2)


# Button
button = Button(text="Calculate", font=("Consolas", 15), command=calculate)
button.grid(row=2, column=1)
button.config(padx=10, pady=10)

# Entry
miles_input = Entry(width=10, font=("Consolas", 15))
miles_input.grid(row=0, column=1)



window.mainloop()
from tkinter import *

def button_clicked():
    print("I'm clicked")
    new_text = raw_input.get()
    my_lbl.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_lbl = Label(text="I'm Label", font=("Arial", 24, "bold"))
my_lbl.config(text="New Text")
# my_lbl.pack()
# my_lbl.place(x=100, y=200)
my_lbl.grid(row=0, column=0)
my_lbl.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="New Button")
# button.pack()
# button.place(x=100, y=170)
button.grid(row=1, column=1)
button2.grid(row=0, column=2)

# Entry
raw_input = Entry(width=10)
print(raw_input)
# row_input.pack()
# row_input.place(x=100, y=190)
raw_input.grid(row=2, column=3)


window.mainloop()
from tkinter import * 


window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height= 300)
window.config(padx=100, pady=100)

#Label 

my_label = Label(text = "I Am a Label", font=("Arial", 24, "italic"))
my_label.config(text = "New Text")
# my_label.grid(column=0, row=0)
# my_label.config(padx=60,pady=85)
my_label["text"] = "New Text"
my_label.pack()


def button_clicked():
    print("I got clicked")
    temi = input.get()
    my_label["text"] = temi

button = Button(text = 'Click Me', command = button_clicked)
# button.grid(column=1, row=1)
button.pack(side = "left")

# new_button = Button(text = 'New Button', command = button_clicked)
# new_button.grid(column=2, row=0)

input = Entry(width = 10)
print(input.get())
# input.grid(column=3, row=2)
input.pack(side = "left")

entry = Entry(width = 30)
entry.insert(END, string="email.nsk.ai@gmail.com")
entry.focus()

entry.pack()

# print(entry.get())

text = Text(height=5, width=50)
text.focus()
text.insert(END, "Talk about yourself in less than a 1000 words,\n DO NOT BE AFRAID OF WHAT IS TO COME")
print(text.get("1.0", END))
text.pack()

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5,
command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100,
command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",
variable=checked_state,
command=checkbutton_used)
checked_state.get()
checkbutton.pack()

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2",value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()













window.mainloop()
from cgitb import text
from tkinter import *

def kilo():
    temi = entry.get()
    km = int(temi)/1000
    kilo_result["text"] = round(km,2)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width = 500, height= 300)
window.config(padx=200, pady=100)

entry = Entry(width = 3)
entry.insert(END, string="0")
entry.focus()
entry.get()
entry.grid(column = 0 ,row = 1 )
# entry.pack()
my_miles = Label(text = "Miles", font=("Arial", 8))
my_miles.grid(column = 0,row=0)
# my_miles.pack()
my_kilo = Label(text = "Kilometer", font=("Arial", 8))
my_kilo.grid(column = 4,row=0)
# my_kilo.pack()
kilo_result = Label(text = "0")
kilo_result.grid(column= 4,row=1)

my_equiv = Label(text = "=", font=("Arial", 15))
my_equiv.grid(column=2,row=1)

calculate = Button(text = 'Calculate',command=kilo)
calculate.grid(column=2,row=4)
window.mainloop()
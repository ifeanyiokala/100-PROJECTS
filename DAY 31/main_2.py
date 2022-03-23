# Import the necessary modules 
import pandas as pd 
import random

from tkinter import * 

# set color and font name
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

# read csv and save to file_save
try:
    file_save = pd.read_csv("data\\Angela.csv")
except FileNotFoundError:
    file_save = pd.read_csv("data\\igbo.csv")

file_dict = file_save.set_index("Igbo")["English"].to_dict()

# intialize fr & en 
fr = en = None

# created a function for when the user gets the correct answer 
def right_choice():
    global fr,en,flip,file_dict  # called the needed global variables 
     # randomly selected a dictionary and asssigned it to fr,en variables 
    fr, en = random.choice(list(file_dict.items())) 
    window.after_cancel(flip)
    canvas.itemconfig(Front_cover,image = white_img)
    canvas.itemconfig(igbo_title,text = "Igbo", fill = "black")
    canvas.itemconfig(igbo_word,text = fr, fill = "black")
    file_dict.pop(fr)  # popped the correct answer from the dataset 
    data = pd.DataFrame(file_dict.items())
    data.to_csv("Angela.csv")  # saved the new dataset into angela.csv
    flip = window.after(3000,eng_change)  # after three seconds, eng_change will be called.

# English translation which is called three seconds after seeing the igbo word 
def eng_change():
    canvas.itemconfig(Front_cover,image =green_img)
    canvas.itemconfig(igbo_title,text = "English", fill = "white")
    canvas.itemconfig(igbo_word,text = en, fill = "white")


# creating the tk window in padding 50,50 
window = Tk()
window.title("Igbo Flashcards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# calls the fuction eng_change to change the word 
# to it's english translation after three seconds
flip = window.after(3000,eng_change)

# gave the window it's necessary dimensions 
canvas = Canvas(width=800, height=526)

# Assigned two images to green_img and white_img
green_img = PhotoImage(file="images\card_back.png")
white_img = PhotoImage(file="images\card_front.png")

# assigned the image white_img into the canvas 
# i also gave it a coordinate posotion
Front_cover = canvas.create_image(400, 263, image=white_img)

# gave the canvas a background color 
# set highlightthickness to 0 
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

# i added some texts to the canvas 
# i assigned them to two variables 
igbo_title = canvas.create_text(400, 130, text="Igbo", fill="black", font=(FONT_NAME, 35))
igbo_word = canvas.create_text(400, 280, text="word", fill="black", font=(FONT_NAME, 35, "bold"))

# expanded the column width of both texts by 2 
canvas.grid(column=0,row=0,columnspan=2)

#green tick
green_image = PhotoImage(file="images\\right.png")
button = Button(image=green_image, highlightthickness=0,command= right_choice)
button.grid(column = 1, row = 1)

#red cross
red_image = PhotoImage(file="images\\wrong.png")
button = Button(image=red_image, highlightthickness=0,command= right_choice)
button.grid(column = 0 ,row = 1)






















window.mainloop()
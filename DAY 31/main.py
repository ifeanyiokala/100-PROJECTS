# from cgitb import text
# from email.mime import image
# from glob import glob
from tkinter import * 
import pandas as pd 
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
temi = pd.read_csv("data\\french_words.csv")
temi_dict = temi.set_index("French")["English"].to_dict()
# print(temi_dict)
# en = fr = None
fr, en = random.choice(list(temi_dict.items()))
print(fr,en)
# temi_random = []


def good_choice():
    global flip,fr,en
    global temi_dict
    window.after_cancel(flip)
    # temi_random = random.choice(list(temi_dict.items()))
    # fr, en = random.choice(list(temi_dict.items()))
    canvas.itemconfig(remi,image = tomato_img)
    canvas.itemconfig(chike,text = "French", fill = "black")
    canvas.itemconfig(chuka,text = fr, fill = "black")
    # print(temi_dict)
    print(fr,en)

    temi_dict.pop(fr)
    data = pd.DataFrame(temi_dict,index=range(len(temi_dict)))
    data.to_csv("Angela.csv",index= False)
    flip = window.after(3000,eng_change)

def choice():
    global fr,en,flip
    window.after_cancel(flip)
    # temi_random = random.choice(list(temi_dict.items()))
    # anji = temi_random[0]
    canvas.itemconfig(remi,image = tomato_img)
    canvas.itemconfig(chike,text = "French", fill = "black")
    canvas.itemconfig(chuka,text = fr, fill = "black")
    flip = window.after(3000,eng_change)

    
def eng_change():
    global fr,en
    canvas.itemconfig(remi,image =new_img)
    canvas.itemconfig(chike,text = "English", fill = "White")
    # she = temi_random[1]
    canvas.itemconfig(chuka,text = en, fill = "White")
    

# def french_change():
    




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
flip = window.after(3000,eng_change)

# temi = pd.read_csv("data\\french_words.csv")
# temi_dict = temi.set_index("French")["English"].to_dict()
canvas = Canvas(width=800, height=526)
new_img = PhotoImage(file="images\card_back.png")
tomato_img = PhotoImage(file="images\card_front.png")
remi = canvas.create_image(400, 263, image=tomato_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
chike = canvas.create_text(400, 130, text="Title", fill="black", font=(FONT_NAME, 35))
chuka = canvas.create_text(400, 280, text="word", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=0,row=0,columnspan=2)

green_image = PhotoImage(file="images\\right.png")
button = Button(image=green_image, highlightthickness=0,command=good_choice)
button.grid(column = 1, row = 1 )


red_image = PhotoImage(file="images\\wrong.png")
button = Button(image=red_image, highlightthickness=0,command=choice)
button.grid(column = 0 ,row = 1)

# abo = True
# while abo:
#     kemi = window.after(3000,eng_change)





























window.mainloop()
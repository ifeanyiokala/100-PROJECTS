from tkinter import * 


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, )



canvas = Canvas(width=240, height=240)
tomato_img = PhotoImage(file="password-manager-start//logo.png")
canvas.create_image(120, 100, image=tomato_img)
canvas.pack()
























window.mainloop()
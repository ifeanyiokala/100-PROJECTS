from tkinter import * 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score :{self.quiz.score}/{self.quiz.question_number} ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        
        self.canvas = Canvas( width=300, height=250, bg ='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            fill="darkblue",
            font=("Arial", 20, "italic"),
            text="Some Question Text"
            )

        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)


        red_image = PhotoImage(file="images\\false.png")
        self.false = Button(image=red_image, highlightthickness=0,command=self.true_pressed)
        self.false.grid(column = 1,row = 2 )
        
        green_image = PhotoImage(file="images\\true.png")
        self.true = Button(image=green_image, highlightthickness=0,command=self.false_pressed)
        self.true.grid(column = 0,row = 2 )



        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz. :)")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        self.score_label.configure(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        # self.window.update

        


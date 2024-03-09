import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        self.questions = questions
        self.current_question_index = 0

        self.question_label = tk.Label(self, text="", wraplength=380)
        self.question_label.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self, text="", variable=self.radio_var, value=str(i))
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor="w")

        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        for i in range(4):
            self.radio_buttons[i].config(text=question["options"][i])

    def next_question(self):
        selected_option = self.radio_var.get()
        if selected_option == "":
            messagebox.showwarning("Warning", "Please select an option.")
        else:
            selected_option = int(selected_option)
            correct_option = self.questions[self.current_question_index]["answer"]
            if selected_option == correct_option:
                messagebox.showinfo("Correct", "Your answer is correct!")
            else:
                messagebox.showerror("Incorrect", "Sorry, your answer is incorrect.")

            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.load_question()
            else:
                messagebox.showinfo("Quiz Completed", "You have completed the quiz.")
                self.destroy()

if __name__ == "__main__":
    questions = [
        {
            "question": "What is the capital of INDIA?",
            "options": ["mumbai", "delhi", "goa", "chennai"],
            "answer": 1
        },
        {
            "question": "What is the largest planet in the solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H", "O", "He", "H2O"],
            "answer": 3
        }
    ]

    app = QuizApp(questions)
    app.mainloop()

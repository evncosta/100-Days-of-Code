# QuizBrain Class - Manages quiz logic and scoring
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0  # Tracks current question index
        self.score = 0            # Tracks correct answers
        self.list = question_list # Stores the question bank

    def still_has_questions(self):
        # Check if more questions remain
        return self.question_number < len(self.list)

    def next_question(self):
        # Display next question and get user input
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question)

    def check_answer(self, user_answer, current_question):
        # Validate answer and update score
        if user_answer.upper() == current_question.answer.upper():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        # Provide feedback and current score
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")

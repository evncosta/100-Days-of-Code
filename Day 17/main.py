# Quiz Game - Main program that runs the quiz from external data
import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create question bank from external data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Randomize question order for variety
random.shuffle(question_bank)

# Initialize quiz with question bank
quiz = QuizBrain(question_bank)

# Main quiz loop - continue while questions remain
while quiz.still_has_questions():
    quiz.next_question()

# Display final results after quiz completion
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

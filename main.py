import random
import data
from question_model import Question
from quiz import Quiz

question_data = data.animals

questions = []
for question in question_data:  
    new_question = Question(question["question"], question["correct_answer"], question["type"], question["incorrect_answers"])
    if question["type"] == "multiple": 
        random.shuffle(new_question.choices)
    questions.append(new_question)

quiz = Quiz(questions)

while quiz.questions_remaining():
    quiz.next_question()

print("Quiz complete!")
print(f"You got {quiz.score} out of {quiz.question_number} questions.")

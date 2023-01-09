import random
import data
from question_model import Question

question_data = data.bird_questions

questions = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    questions.append(new_question)

print(questions)
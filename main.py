import random
import data
from question_model import Question
from quiz_brain import QuizBrain

question_data = data.bird_questions

questions = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    questions.append(new_question)

quiz = QuizBrain(questions)
quiz.next_question()
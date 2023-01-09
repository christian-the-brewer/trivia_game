
class QuizBrain:
    def __init__(self, questions):
        self.questions_list = questions
        self.question_number = 0
        self.score = 0

    def questions_remaining(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"{answer} is the answer.")
        print(f"Score: {self.score} out of {self.question_number}")


   
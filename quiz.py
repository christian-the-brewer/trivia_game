
class Quiz:
    def __init__(self, questions):
        self.questions_list = questions
        self.question_number = 0
        self.score = 0
        self.choice_dict = {}

    def questions_remaining(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        #sort out the true/false
        if current_question.type == "boolean":
            user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False?\n")
            self.check_answer(user_answer, current_question.answer)
        else:
            #handle multiple choice
            self.choice_dict = dict(zip(["a","b","c","d"], current_question.choices))
            a = self.choice_dict["a"]
            b = self.choice_dict["b"]
            c = self.choice_dict["c"]
            d = self.choice_dict["d"]
            user_answer = input(f"Q.{self.question_number}: {current_question.text}\nA: {a}\nB: {b}\nC: {c}\nD: {d}\n").lower()
            if user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d":
                user_answer = self.choice_dict[user_answer]
            self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, answer):
        #first thing is to accept 't' or 'f' answers
        if user_answer.lower() == "t":
            user_answer = "True"
        elif user_answer.lower() == "f":
            user_answer = "False"
        if user_answer.lower() == answer.lower():
            print("Correct!")
            self.score += 1 # increase score
        else:
            print("Wrong!")
        print(f"{answer} is the answer.")
        print(f"Score: {self.score} out of {self.question_number}")


   
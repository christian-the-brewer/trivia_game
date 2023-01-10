#question class

class Question:
    def __init__(self, text, answer, type, incorrect_answers):
        self.text = text
        self.answer = answer
        self.type = type
        self.incorrect_answers = incorrect_answers
        self.choices = []
        self.choices.extend(self.incorrect_answers)
        self.choices.append(self.answer)
        
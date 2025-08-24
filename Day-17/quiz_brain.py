class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        score = 0
        if answer.lower() == current_question.answer.lower():
            score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_question.answer}")
            print(f"Your current score is: {score}/{self.question_number}")

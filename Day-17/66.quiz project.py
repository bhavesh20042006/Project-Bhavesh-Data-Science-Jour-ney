from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    quesion_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(quesion_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.question_number < len(question_bank):
    quiz.next_question()
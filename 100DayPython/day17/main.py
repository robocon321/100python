from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz_brain = QuizBrain(question_bank)

while(quiz_brain.still_has_questions()):
    quiz_brain.next_question()

print(f"Your final score: {quiz_brain.score}")
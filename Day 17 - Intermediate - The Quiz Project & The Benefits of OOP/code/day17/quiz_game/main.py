from data import get_questions
from question_model import Question
from quiz_brain import QuizBrain

# TODO2 - Fazer um loop 'for' para iterar sobre question_data
# TODO3 - Criar um objeto Question para cada valor de question_data
# Todo4 - Incluir cada objeto Question no question_bank (lista)
# TODO11 - Usar o loop while para mostrar a proxima pergunta ate terminar
# TODO14 - Informar o usuario que ele finalizou o Quiz e mostrar a pontuacao final

question_bank = []

# for question in question_data:
#     obj = Question(question["text"], question["answer"])
#     question_bank.append(obj)

for question in get_questions():
    obj = Question(question["text"], question["answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)


while quiz.stll_has_questions():
    quiz.new_question()

print("You've complete the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.num_questions}")



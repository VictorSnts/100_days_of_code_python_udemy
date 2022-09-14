# TODO5 - Criar uma classe chamada QuizBrain
# TODO6 - Escrever o construtor com os atrubutos question number (valor 0) e question_list (input da classe)
# TODO7 - Receba uma question com o indice question_number
# TODO8 - use input para mostrar a pergunta ao usuario e perguntar pela resposta
# TODO9 - Criar um metodo chamado still-has_questions()
# TODO10 - Retornar um boolean dependendo do valor da questao
# TODO12 - Criar um metodo que checa se a resposta esta correta
# TODO13- Criar um atributo de pontuacao e incrementar a cada resposta certa


def valida_entrada(entrada):
    entradas_validas = ["false", "true"]
    if entrada in entradas_validas:
        return True
    else:
        return False


def check_answer(correct_answer, user_answer):
    if user_answer == correct_answer:
        print("You got it right!")
        return True
    else:
        print(f"That's Wrong. \nThe correct answer is {correct_answer}.")
        return False


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.num_questions = len(question_list)
        self.score = 0

    def new_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.question} (True/False)?: ").lower()
        if valida_entrada(user_answer):
            if check_answer(question.answer.lower(), user_answer):
                self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}\n")
        else:
            print("Invalid Option!")
            self.question_number -= 1

    def stll_has_questions(self):
        return self.question_number < self.num_questions

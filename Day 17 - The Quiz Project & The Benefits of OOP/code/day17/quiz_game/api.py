import requests as rq

request = rq.request("GET", "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")

dados_brutos = request.json()
dados = []

for registro in dados_brutos['results']:
    question = {
        "text": registro["question"],
        "answer": registro["correct_answer"]
    }
    dados.append(question)




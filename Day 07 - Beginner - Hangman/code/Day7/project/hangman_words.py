import random

words = ["aviao", "elefante", "bola", "bebe", "peixe", "futebol", "beliscao", "basquete", "triste", "gato", "golfe",
         "tesoura", "colher", "pular", "galinha", "sapo", "espirro", "martelo", "violao", "aplaudir", "tosse",
         "chifres", "pinguim", "chorar", "rabo", "piada", "celular", "cachorro", "pato", "sofa", "fotografo", "bale",
         "pipa", "cafe", "taxi", "cadeira", "onibus", "elevador", "bicicleta", "fogao", "copo", "orelhas", "chocolate",
         "pescador", "notebook", "lapis"]


def get_word():
    return random.choice(words)

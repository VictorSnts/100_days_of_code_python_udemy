from time import sleep

desligar = False

recursos = {
    "Agua": 300,
    "Cafe": 100,
    "Leite": 200,
    "Dinheiro": 0.00
}

EXPRESSO = {
    "Nome": "Café Expresso",
    "Agua": 50,
    "Cafe": 18,
    "Leite": 0,
    "Preco": 1.50
}

COM_LEITE = {
    "Nome": "Café com Leite",
    "Agua": 200,
    "Cafe": 24,
    "Leite": 250,
    "Preco": 2.50
}

CAPUCCINO = {
    "Nome": "Capuccino",
    "Agua": 300,
    "Cafe": 24,
    "Leite": 100,
    "Preco": 3.00
}


def desligar_maquina():
    """Desliga a maquina de café"""
    global desligar
    desligar = True


def report():
    """Informa os recursos disponiveis na maquina"""
    print(f"""
    Agua: {recursos['Agua']} ML
    Cafe: {recursos['Cafe']} G
    Leite: {recursos['Leite']} ML
    Dinheiro: R$ {recursos['Dinheiro']}
    """)


def define_tipo_cafe(cafe_informado):
    """Retorna a constante referente ao tipo de cafe_escolhido escolhido"""
    if cafe_informado == "expresso":
        return EXPRESSO
    elif cafe_informado == "com leite":
        return COM_LEITE
    elif cafe_informado == "capuccino":
        return CAPUCCINO


def get_tipo_cafe():
    """Pergunta para o usuario qual cafe_escolhido ele gostaria e faz as devidas validacoes da entrada"""
    entrada_usuario = input("Qual café você gostaria? (expresso/com leite/capuccino):")
    if (entrada_usuario == "expresso") or (entrada_usuario == "com leite") or (entrada_usuario == "capuccino"):
        return define_tipo_cafe(entrada_usuario)
    elif entrada_usuario == "desligar":
        print("A maquina será desligada!")
        desligar_maquina()
        pass
    elif entrada_usuario == "report":
        report()
        pass
    else:
        print("Tipo de café invalido!")
        get_tipo_cafe()


def recursos_disponiveis(cafe):
    """Verifica se os recursos disponiveis sao suficiente para o cafe desejado"""
    if recursos["Agua"] < cafe["Agua"]:
        print("Desculpe, não há água suficiente")
        return False
    elif recursos["Cafe"] < cafe["Cafe"]:
        print("Desculpe, não há café suficiente")
        return False
    elif recursos["Leite"] < cafe["Leite"]:
        print("Desculpe, não há leite suficiente")
        return False
    else:
        return True


def devolve_troco(troco):
    """Devolve o troco para o usuario"""
    print(f"Aqui esta seu troco: R${troco}")


def recebe_moedas(cafe):
    """Recebe as quantidade de moedas do usuario de acordo com o necessario"""
    valor = cafe["Preco"]

    print("Por favor, insira as moedas: ")
    m_1_real = int(input("1 real: ")) * 1
    total_inserido = m_1_real
    if total_inserido < valor:
        m_50_cent = int(input("50 centavos: ")) * 0.50
        total_inserido += m_50_cent
    if total_inserido < valor:
        m_25_cent = int(input("25 centavos: ")) * 0.25
        total_inserido += m_25_cent
    if total_inserido < valor:
        m_10_cent = int(input("10 centavos: ")) * 0.10
        total_inserido += m_10_cent
    if total_inserido < valor:
        m_5_cent = int(input("5 centavos: ")) * 0.05
        total_inserido += m_5_cent

    if total_inserido < valor:
        print("O valor inserido é menor que o preco do seu cafe_escolhido! \n"
              "Operação Cancelada. Suas moedas serão devolvidas.\n"
              "Tente novamente.\n\n")
        return False
    elif total_inserido > valor:
        devolve_troco(total_inserido - valor)
        return True
    elif total_inserido == valor:
        return True


def deduzir_recursos(cafe):
    """Deduz os recursos usados para preparar o café e soma o preco no caixa"""
    global recursos
    recursos["Agua"] -= cafe["Agua"]
    recursos["Cafe"] -= cafe["Cafe"]
    recursos["Leite"] -= cafe["Leite"]
    recursos["Dinheiro"] += cafe["Preco"]


def fazer_cafe(cafe):
    """Faz o café"""
    deduzir_recursos(cafe)
    print(f"Preparando o seu {cafe['Nome']}...")
    sleep(5)
    print(f"Seu {cafe['Nome']} está pronto.\n\n\n")


while not desligar:
    entrada = get_tipo_cafe()
    if entrada is not None:  # É uma entrada válida
        cafe_escolhido = entrada
        if recursos_disponiveis(cafe_escolhido):  # Tem recursos disponiveis
            if recebe_moedas(cafe_escolhido):  # Recebeu dinheiro sufiiciente para o café
                fazer_cafe(cafe_escolhido)
            else:  # nao recebeu dinheiro sufiiciente para o café
                pass
        else:  # Não tem recursos disponiveis
            pass
    else:  # Não é uma entrada válida
        pass

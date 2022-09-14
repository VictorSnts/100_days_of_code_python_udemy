# # Criando uma classe
# class User:
#     # Criando um construtor
#     def __init__(self, id, username):
#         # Aqui inicializamos ou atribuimos valores aos atributos da classe e o que deve acontecer ao instanciar um novo
#         #   objeto desse tipo
#         print("Novo usuario criado")
#         self.id = id
#         self.username = username
#         self.followers = 0 # Aqui definimos um argumento com valor padrao na instanciacao do objeto
#
#     pass
#
#
# # Usando a classe:
# user1 = User("001", "vicsantos")  # Instanciando um objeto passando o valor dos atributos
# user2 = User("002", "lucsantos")
# print("\n")
#
# # Usando os argumentos da classe
# print(user1.id)
# print(user1.username)
# # print(user1.followers)
#
# print(user2.id)
# print(user2.username)
# # print(user2.followers)
# print("\n")
#
# # Alterando o valor dos argumentos
# user1.followers += 100
# user2.followers += 200
#
# print(user1.followers)
# print(user2.followers)
# print("\n")

# ------------------------------------------------------
class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bancos = 5
        self.estepe = True
        self.tipo_pneus = "Radial"

    def get_info(self):
        print(f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cor: {self.cor}
        Bancos: {self.bancos}
        Estepe: {self.estepe}
        Marca: {self.marca}
        Tipo Pneus: {self.tipo_pneus}
        """)

    def inicia_modo_corrida(self):
        print("Retirando bancos, estepe e trocando os pneus")
        self.bancos = 1
        self.estepe = True
        self.tipo_pneus = "Slick"

    def pintar(self, nova_cor):
        self.cor = nova_cor


carro1 = Carro("Honda", "Civic", "Prata")
carro2 = Carro("Toyota", "Corolla", "Preta")

carro1.get_info()
# carro2.get_info()

carro1.inicia_modo_corrida()
carro1.pintar("Azul")

carro1.get_info()


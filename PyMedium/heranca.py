#Herdando classes

print("Criar classe Funcionário e depois criar uma classe Admin, herdando de Funcionário")

#declaração da classe Funcionario
class Funcionario():
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
    def dados(self):
        return {'nome':self.nome, 'salario':self.salario}

#criando um objeto/instância da classe Funcionário
fabio = Funcionario("Fabio",6000)
#Acessando métodos do objeto da classe Funcionário
print(fabio.dados())

#Herdando da classe funcionário para criar uma nova classe chamada Admin
class Admin(Funcionario):
    def __init__(self,nome, salario):
        super().__init__(nome, salario) #realizo os mesmos métodos do construtor da classe pai
    def atualizar_dados(self,nome): #método novo que não existe na classe pai
        self.nome = nome
        return self.dados()

#criando uma instância de Admin
fernando = Admin('Fernando',14000)

print(fernando.dados())
#utilizando o método exclusivo da classe Admin para modificar o atributo Nome
fernando.atualizar_dados("Fernandinho")
print(fernando.dados())
class Funcionario():
    aumento = 1.04
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}
    def aplicarAumento(self):
        self.salario = self.salario * self.aumento
    @classmethod #ClassMethod realiza a função e aplica o resultado na classe, e não apenas ao objeto instanciado
    def definirNovoAumento(cls, novoAumento):
        cls.aumento = novoAumento #altera o valor da variável original "aumento" para um novo valor
    @staticmethod #StaticMethod tem relação com a classe em questão, mas não exige nenhum argumento dela
    def diaUtil(dia):
        #segunda-feira = 0
        # ~~~~~
        #domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

fabio = Funcionario('Fábio', 3500)
print(fabio.dados())

#Chamando a função para aplicar o aumento ao objeto Fabio
print("Fabio depois do aumento")
fabio.aplicarAumento()
print(fabio.dados())

#Alterando o valor de Aumento para toda a classe Funcionario
Funcionario.definirNovoAumento(1.05)
fabinho = Funcionario("Fabinho", 3500)
#Criando novo objeto do tipo Pessoa
print("Nova Pessoa: Fabinho")
print(fabinho.dados())
print("Fabinho recebe o mesmo salário que Fabio, e passará por reajuste após o valor do aumento ter sido atualizado")
fabinho.aplicarAumento()
print(fabinho.dados())

print("Conferindo dias úteis")
#Usando a lib datetime para calcular o dia da semana em que determinada data caiu
import datetime
minhaData = datetime.date(2019,4,11)# quinta-feira
print("Printando uma quinta-feira")
print("É dia útil?",Funcionario.diaUtil(minhaData))
print("Printando uma Sexta-feira")
minhaData = datetime.date(2019,4,12)# sexta-feira
print("É dia útil?",Funcionario.diaUtil(minhaData))
print("Printando um Sábado")
minhaData = datetime.date(2019,4,13)# Sábado
print("É dia útil?",Funcionario.diaUtil(minhaData))
print("Printando um Domingo")
minhaData = datetime.date(2019,4,14)# Domingo
print("É dia útil?",Funcionario.diaUtil(minhaData))
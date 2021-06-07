print("Estudando Classes e Objetos em Python")

jogadorLoteria1={
    'nome':'Pedro',
    'numeros':(13,4,52,23,68,83)
}

jogadorLoteria2={
    'nome':'Pedro',
    'numeros':(13,4,52,23,68,83)
}

print(jogadorLoteria1)
print(jogadorLoteria2)

print("Os valores de jogadorLoteria1 e jogadorLoteria2 são iguais? ", jogadorLoteria1==jogadorLoteria2)

#Classes e Objetos

#criando classe JogadorLoteria com os mesmos valores que foram dados aos objetos acima
class JogadorLoteria:
    def __init__(self):
        self.nome = 'Pedro'
        self.numeros = (13,4,52,23,68,83)
    def total(self):
        return sum(self.numeros)

#instanciando a classe JogadorLoteria

jogador1 = JogadorLoteria()
jogador2 = JogadorLoteria()

print("Printando os atributos e valores dos métodos de Jogador1:")
print(jogador1.nome)
print(jogador1.numeros)
print(jogador1.total())

print("Printando os atributos e valores dos métodos de Jogador2:")
print(jogador2.nome)
print(jogador2.numeros)
print(jogador2.total())

print("Os objetos jogador1 e jogador2 são iguais? ", jogador1 == jogador2)

class JogadorFutebol:
    def __init__(self, nome, time, gols):
        self.nome = nome
        self.time = time
        self.gols = gols
    def marcarGol(self):
        return self.gols + 1

boleiro1 = JogadorFutebol('CR7', 'RealMadrid', 600)
boleiro2 = JogadorFutebol('Messi', 'Barcelona', 600)

print("Uma besta enjaulada chamada",boleiro1.nome)
print("Agora o {} já marcou {} gols".format(boleiro1.nome,boleiro1.marcarGol()))

print("O nome do boleiro 2 é:",boleiro2.nome)
print("O boleiro 2 já marcou", boleiro2.gols, "gols")
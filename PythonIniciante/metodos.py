print("Olá, nesse arquivo aprenderemos sobre as funções no Python, ou Métodos")

def meu_metodo():
    print("Olá mundo vindo da função meu_metodo")

meu_metodo()

def somar(a,b):
    soma = a+b
    return soma

#printa e executa o resultado da função soma
somar(40,28)

#função que retorna o tamanho de uma string
def tamanhoString(frase):
    tamanho = len(frase)
    return tamanho

print(tamanhoString("Dois pratos de tigres para três trigos tristes"))

def valorAbsoluto(numero):
    absoluto = abs(numero)
    return absoluto

print(valorAbsoluto(-76))


#definindo uma lista em python
#soma os valores de uma lista
lista = [1,2,3,4,5,6,7]
print("Agora vamos somar os valores dessa lista:",lista)
print(sum(lista))

print("vamos pegar o menor e o maior valor da lista")
#usando duas formas diferentes de concatenação
print("O menor valor da lista é: "+ str(min(lista))+", e o maior valor é:", max(lista))

print("Agora vamos usar a função Round() para arredondar valores")
print("O valor arredondado de 11.7 é:", round(11.7))
print("O valor arredondado de 11.78567 é:", round(11.78567))


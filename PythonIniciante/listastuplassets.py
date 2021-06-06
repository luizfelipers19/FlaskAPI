#Nesse arquivo estudaremos Listas, Tuplas e Sets

nota1 = 3
nota2 = 5
nota3 = 6
nota4 = 2
nota5 = 8

print("A média das 5 notas é:",(nota1+nota2+nota3+nota4+nota5)/5)

#ao invés de declararmos diversas variáveis para guardar as notas, 
#podemos guardar as notas dentro de uma lista

notas = [3, 5, 6, 2, 8]
print(notas)
print("A média das notas é:", sum(notas)/len(notas))

print("Podemos também adicionar um valor no final da lista usando o comando .append()")
notas.append(10)
print("a lista de notas agora contém essas notas:", notas)

print("Usando o comando .extend(), podemos adicionar múltiplos valores numa lista")
notas.extend((4,6,3,7))
print("após o comando extend, a lista de notas agora contém essas notas:", notas)

#definindo uma função para calcular a média das notas
print("Essa função calculará a média das notas")

def mediaNotas(listaNotas):
    media = sum(listaNotas)/len(listaNotas)
    return media

print("A média das notas na lista de notas é:", mediaNotas(notas))

print("Acessando o primeiro elemento da lista")

print(notas[0])

print("Acessando o último elemento da lista")
print(notas[len(notas)-1]) #pegando o tamanho da lista e subtraindo 1 para pegar o último elemento da lista

#Tuplas
print()
print("-------------------------------------")
print("Tuplas")

#Tuplas não podem ser modificadas
tupla = (3,4,5,6)
print(tupla)
#tuplas são como as listas, porém, as tuplas são imutáveis
print("podemos adicionar elementos na tupla, mas essa tupla não será modificada, e sim, a variável será destruída e outra com o mesmo nome será criada com os novos valores")
#utilizando a operação de somar duas tuplas, podemos anexar valores ao fim da tupla que será 'modificada'

tupla += (7,)
print(tupla)

#SETS
print()
print("-------------------------------------")
print("Sets")
 #Sets são tipos de conjuntos do Python, onde são armazenados apenas valores únicos

listaNota =[1,2,3,5,6,5,7,9,8,3,2,4,1,9,6,4,3,5,6]
#para ilustrar o que é um set, primeiramente criaremos uma lista
# com uma série de valores repetidos e imprimiremos essa lista
print("Essa é a lista de notas:",listaNota)

#agora transformaremos essa lista em um set
print("Essa é a nossa lista de notas transformada em set:", set(listaNota))

#o set da lista acima equivale a criar o set manualmente
setNota ={1,2,3,5,6,5,7,9,8,3,2,4,1,9,6,4,3,5,6}
print("Esse é o nosso set quando declarado diretamente como set e usando chaves para envolver os valores:", setNota)

#podemos adicionar valores ao set utilizando a função .add
setNota.add(12)
print("Nosso set após adicionarmos um valor inédito:", setNota)

#adicionando um valor repetido, nosso set não adicionará esse valor
setNota.add(1)
print("Nosso set após adicionarmos um valor repetido permanece o mesmo:", setNota)

#podemos também adicionar valores de outros tipos num set
setNota.add("Valor")
print(setNota)

#adicionando múltiplos valores ao set com a função .update
setNota.update(["C","OutroValor", "Prata","hsuahu", "outrovalor"])
print(setNota)
print(sorted(set(str(setNota))))
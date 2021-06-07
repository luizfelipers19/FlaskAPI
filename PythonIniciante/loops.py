variavel = "ola"

print(len(variavel))

#printando as letras de uma variável já definida
for letra in variavel:
    print(letra)


#definindo função para printar todas as letras de uma sting passada por parâmetro
def printLetras(frase):
    for letra in frase:
        print(letra)

print(printLetras("Apipocadapanteranegraeracommanteiga"))

#definindo uma lista manualmente
lista = [0,1,2,3,4,5,6,7,8,9,10]
print(lista)

#função RANGE
#range(start,stop,step)
for letra in range(10+1):
    print(letra)

listaAutomatica = list(range(10+1))
print(listaAutomatica)

print("Preenchendo uma lista com elementos ímpares de 1 até 20")
print(list(range(1,21,2)))

print("Preenchendo uma lista com números pares de 0 a 10")
numerospares = list(range(0,11,2))
print(numerospares)

#multiplicando todos os elementos da lista por dois **Usando list comprehension**
listamultiplicada = [element * 2 for element in numerospares]

print(listamultiplicada)

print()
print("------------------------------------------")
print("WHILE")

x = 0
while x <=10: #X foi definido como 0, enquanto for menor ou igual a 10, executará o corpo do loop
    print(x**2)
    x +=1 # INCREMENTO
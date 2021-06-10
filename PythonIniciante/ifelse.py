#Condicionais em Python: IF e Else

continuar = True

if continuar:
    print("Continue")

pessoas_conhecidas = ['João',"Marcelo", "Renato", "Rodrigo", "Theo", "Gabriel", "Celso"]

pessoa= input("Entre com o nome de uma pessoa: ")
print(pessoa)

#se o valor da variável pessoa estiver na lista de pessoas_conhecidas
if pessoa in pessoas_conhecidas:
    print("Você conhece {}".format(str(pessoa)))
else: #Se o valor de pessoa não estiver na lista de pessoas_conhecidas
    print("Você não conhece {}" .format(str(pessoa)))

a = int(input("Digite um valor para a variável A: "))
b = int(input("Digite um valor para a variável B: "))
c = 10

if(a > b):
    print("o valor de A:", a, "é maior que o valor de B:", b)
else:
    print("O valor de B:",b, "é maior que o valor de A:",a)

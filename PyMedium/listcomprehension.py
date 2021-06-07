print("List Comprehension")

#Operações em listas com listcomprehensions

print([x for x in range(5)])

print("printando a lista acima com os seus valores multiplicados por 5")
print([x*5 for x in range(5)])

print("printando uma lista que segue um padrão condicional")
print([n for n in range(20) if n%2 ==1])

print("criando uma lista de pessoas, mas sem padrão de escrita, para ser arrumado com list comprehension")

pessoas = ['Ana', 'PEDro', 'joao', 'mAx', 'dougLAS', 'lUIz','felipe']
print(pessoas)
print("Arrumando a lista de pessoas: ")
pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas  ]
print(pessoas_normalizadas)
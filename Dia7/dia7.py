it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))#1.1

it_companies.add("Twitter")#1.2

print(it_companies)

it_companies.add("Rockstar")#1.3
it_companies.add("Rexona")
it_companies.add("Panasonic")

print(it_companies)

it_companies.remove("Microsoft")#1.4, 1.5
it_companies.discard("Discard")#1.4, 1.5

##remove(item): Se o item não estiver presente no conjunto, o Python retornará um erro do tipo KeyError. Isso interrompe a execução do programa a menos que o erro seja tratado.
##discard(item): Se o item não estiver presente no conjunto, o Python não fará nada e o programa continuará rodando normalmente, sem retornar erros.

print(it_companies)

C = A.union(B)#2.1

print(C)

print(A.intersection(B))#2.2

print(A.issubset(B))#2.3

print(A.isdisjoint(B))#2.4

C = A.union(B)#2.5

print(C)

C = B.union(A)#2.5

print(C)

print(A.symmetric_difference(B))#2.6

del it_companies #2.6
del A
del B
del C

ages = set(age)#3.1

if (len(ages)> len(age)):
    print("Set é maior que a Lista!!")
elif(len(ages) < len(age)):
    print("Lista é maior que a Set!!")
else:
    print("Ambos são iguais!!")

#3.2
## String: É uma coleção de um ou mais caracteres colocados entre aspas simples, duplas ou triplas
## As aspas triplas são usadas quando a string ocupa mais de uma linha

##List (Lista): É uma coleção ordenada que permite armazenar itens de diferentes tipos de dados 
##Elas são comparadas a "arrays" em outras linguagens, como JavaScript

##Tuple (Tupla): Assim como a lista, é uma coleção ordenada de diferentes tipos de dados 
##A diferença fundamental é que as tuplas são imutáveis, o que significa que não podem ser modificadas depois de criadas

##Set (Conjunto): É uma coleção de itens que não é ordenada
##Além disso, ao contrário de listas e tuplas, um conjunto armazena apenas itens únicos, funcionando de forma semelhante aos conjuntos matemáticos

print("Característica\tString\tLista\tTupla\tConjunto\nOrdenado\tSim\tSim\tSim\tNão\nMutável\t\tNão\tSim\tNão\tSim(pode-se adicionar/remover)\nItens Únicos\tNão\tNão\tNão\tSim(Apenas únicos)")

print("Diferenças entre String,Lista,Tupla e Conjunto:")
print("String: É uma coleção de um ou mais caracteres colocados entre aspas simples, duplas ou triplas")
print("\n")
print("List (Lista): É uma coleção ordenada que permite armazenar itens de diferentes tipos de dados")
print("\n")
print("Tuple (Tupla): Assim como a lista, é uma coleção ordenada de diferentes tipos de dados\nA diferença fundamental é que as tuplas são imutáveis, o que significa que não podem ser modificadas depois de criadas")
print("\n")
print("Set (Conjunto): É uma coleção de itens que não é ordenada\nAlém disso, ao contrário de listas e tuplas, um conjunto armazena apenas itens únicos, funcionando de forma semelhante aos conjuntos matemáticos")#3.2

frase = "I am a teacher and I love to inspire and teach people"#3.3

palavras = frase.split()

print(palavras)

palavras_únicas = set(palavras)

print(f"Palavras únicas:{palavras_únicas}")

print(f"Quantidade:{len(palavras_únicas)}")#3.3



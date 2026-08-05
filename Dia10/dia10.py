for i in range(11):#1.1
    print(i)
print("\n")

for i in range(10,0,-1):#1.2
    print(i)
print("\n")

for i in range(1,8,1):#1.3
    print("#"*i)
print("\n")

for i in range(8):
    for j in range(8):
        print("#",end= " ")
    print()#1.4
print("\n")

for i in range(0,11,1):
    for j in range(0,11,1):
        if i == j:
            print(f"{i} X {j} = {i*j}")#1.5
print("\n")

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in range(len(lista)):
    print(lista[i])#1.6
print("\n")

for i in range(0,100,1):#1.7
    if i % 2 == 0 :
        print(i)
print("\n")

for i in range(0,100,1):#1.8
    if i % 2 == 1:
        print(i)
print("\n")

soma = 0#2.1
for i in range(0,101,1):
    soma = soma + i
print(f"Soma = {soma}")
print("\n")

soma_pares = 0#2.2
for i in range(0,101,1):
    if i % 2 == 0:
        soma_pares = soma_pares + i
print(f"Soma (pares) = {soma_pares}")

soma_impares = 0
for i in range(0,101,1):
    if i % 2 == 1:
        soma_impares = soma_impares + i
print(f"Soma (impares) = {soma_impares}")#2.2
print("\n")

frutas = ['banana', 'orange', 'mango', 'lemon']#3.2

for i in range((len(frutas)-1),-1,-1):
    print(frutas[i])
print("\n")

#1,2,3
list = ["maça","banana","limão","uva","laranja"]#Antes Vazia
print(len(list))#3
for i in (0,4,2):
    print(list[i])#4

#5
dados_aleatorios = ["Jadiel",20,1.72,False,"Rua Álvaro de Andrade 268"]
empresas = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#7
print(empresas)
print(len(empresas))

for i in (0,6,3):
    print(empresas[i])#9

empresas.remove("Microsoft")#10
print(empresas)#10

empresas.insert(3,"IT company")#11 e 12
print(empresas)

empresas.remove("Amazon")#12+1
empresas.insert(6,"AMAZON")#12+1
print(empresas)#12+1

empresas.append('#; ')#12+2
print(empresas)

if "Rockstar" in empresas:
    print("Rockstar pertence a lista")
else:
    print("Rockstar não pertence a lista")#15

empresas.sort()#16
print(empresas)#16

empresas.reverse()#17
print(empresas)#17

tres_primeiras = empresas[:3]#18
tres_ultimas = empresas[-3:]#19

print(tres_primeiras)
print(tres_ultimas)

meio = empresas[3:4]#20

print(meio)

empresas.remove(empresas[0])#21
print(empresas)
empresas.remove(empresas[3])#22
print(empresas)
empresas.remove(empresas[5])#23
print(empresas)
empresas.clear()#24
print(empresas)
del empresas #25

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

print(full_stack)

full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

#Fim da Parte 1

#Parte 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

ages.insert(0,19)
ages.insert(11,26)
print(ages)

mediana = ages[5:6]
print(mediana)

media = sum(ages)/len(ages)
print(media)

range = ages[11] - ages[0]
print(range)

min = min(ages)
max = max(ages)

diff_min = abs(min - media)
diff_max = abs(max - media)

print(diff_max)
print(diff_min)

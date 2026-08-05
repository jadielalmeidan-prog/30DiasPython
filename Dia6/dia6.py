tuple = ()#1.1

irmãos = ("Ryan","Seiya","Yusuke")#Nomes Imaginários;1.2 , 1.3;

irmãs = ("Yasmin","Esther","Gabriela")#Nomes Imaginários;1.2 , 1.3;

quant_irmãos = irmãos + irmãs #1.3

print(quant_irmãos)#1.3

print(len(quant_irmãos))#1.4

parentes = ("Gidel","Osmarina")

familia = quant_irmãos + parentes #1.5

print(familia)#1.5

*quant_irmãos, pai , mãe = familia#2.1

print(f"Irmãos: {quant_irmãos}")#2.1
print(f"Pai: {pai}")#2.1
print(f"Mãe: {mãe}")#2.1

del tuple
del familia

frutas = ("Maça","Banana","Laranja")#2.2

vegetais = ("Alface","Cenoura","Batata")#2.2

produtos_animais = ("Carne","Leite","Ovos")#2.2

comidas = frutas + vegetais + produtos_animais#2.2

print(comidas)#2.2

Comidas_lista = list(comidas)#2.3

print(Comidas_lista)#2.3

n = len(comidas)#2.4

meio = n // 2

if n % 2 != 0:
    meio_item = comidas[meio:meio+1]
else:
    meio_item = comidas[meio-1:meio+1] 

print(meio_item)#2.4

tres_primeiros = comidas[:3]#2.5

print(tres_primeiros)

tres_ultimos = comidas[-3:]

print(tres_ultimos)#2.5

del comidas#2.6
del Comidas_lista#2.6

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')#2.7

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)#2.7
#1 a 3

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
num_complexo = complex(input("Digite um número complexo: "))
print(f"Sua idade é: {idade}")
print(f"Sua altura é: {altura} metros")
print(f"O número complexo digitado é: {num_complexo}")

#4: Área do triângulo

altura_triangulo = int(input("Digite a altura do triângulo(inteiro): "))
base_triangulo = int(input("Digite a base do triângulo(inteiro): "))
area = (base_triangulo * altura_triangulo) / 2
print(f"A área do triângulo é: {area}")

#5 Perímetro do triângulo
a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))
perimetro = a + b + c
print(f"O perímetro do triângulo é: {perimetro}")

#6: Área do retângulo

altura_retangulo = int(input("Digite a altura do retângulo(inteiro): "))
base_retangulo = int(input("Digite a base do retângulo(inteiro): "))
area_retangulo = base_retangulo * altura_retangulo
print(f"A área do retângulo é: {area_retangulo}")

#7: Área do círculo//Comprimento do círculo

raio = int(input("Digite o valor do raio do círculo(inteiro): "))
area_circulo = 3 * (raio ** 2)
comprimento_circulo = 2 * 3 * raio
print(f"A área do círculo é: {area_circulo}")
print(f"O comprimento do círculo é: {comprimento_circulo}")

#8,9,10:Declive/Distância euclidiana
import math

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))
declive = (y2 - y1) / (x2 - x1)
x = (x2 - x1)
y = (y2 - y1)
dist = math.sqrt(x**2 + y**2)
print(f"O declive da linha é: {declive}")
print(f"A distância euclidiana é: {dist}")

#11:Calculo do Y// X = -3 
x = int(input("Digite o valor de x: "))
y = (x**2) + 6 * x + 9
while (y!= 0):
    x = int(input("Digite o valor de x: "))
    y = (x**2) + 6 * x + 9
if y == 0:
    print(f"O valor de x para o qual y = 0 é: {x}")
    print("O valor de y é igual a zero, encerrando o programa.")

#12 a 15

palavra1 = input("Digite a palavra 1: ")
palavra2 = input("Digite a palavra 2: ")

print(f"A Quantidade de letras da palavra 1 é: {len(palavra1)}")
print(f"A Quantidade de letras da palavra 2 é: {len(palavra2)}")

if len(palavra1) > len(palavra2):
    print(f"A palavra 1 é maior que a palavra 2")
elif len(palavra1) < len(palavra2):
    print(f"A palavra 2 é maior que a palavra 1")
else:
    print(f"As palavras possuem o mesmo tamanho")
if "on" in palavra1 and "on" in palavra2:
    print(f"A palavra 1 contém a substring 'on'")
    print(f"A palavra 2 contém a substring 'on'")
frase = "I hope this course is not full of jargon"

if "jargon" in frase:
    print(f"A frase contém a palavra 'jargon'")

#16

texto = "python"
print(f"O texto é: {type(len(texto))}")
print(f"O texto é: {len(texto)}")
texto = float(len(texto))
print(f"O texto é: {type(texto)}")
print(f"O texto é: {texto}")
texto = "python"
print(f"O texto é: {type(texto)}")
print(f"O texto é: {texto}")
#17
num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")
#18 a 20
print(float(7/3) is int(2.7))
print("10" is 10)
print(int(9.8) is 10)

#21

horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = int(input("Digite o valor recebido por hora: "))
salario = horas_trabalhadas * valor_por_hora
print(f"O salário semanal é: {salario}")

#22

anos = 100

segundos = anos * 365 * 24 * 60 * 60
print(f"O número de segundos em {anos} anos vividos é: {segundos}")

#23

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")

#Dia 2/30 dias de programação em python
#Level 1
nome, sobrenome, pais, cidade = "Júlio", "Lima", "Brasil", "Fortaleza"
nome_completo = nome + " " + sobrenome 
idade,ano = 50, 2026
is_married, is_light_on, is_true = True, True, False

print("Nome Antigo:", nome)
print("Sobrenome Antigo:", sobrenome)
print("País Antigo:", pais)
print("Cidade Antiga:", cidade)

#Level 2.1
print(type(nome))
print(type(sobrenome))
print(type(pais))
print(type(cidade))
print(type(idade))
print(type(ano))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
#Level 2.2
print(f"O comprimento do nome é: {len(nome)}")
#Level 2.3
if len(nome) > len(sobrenome):
    print("O nome é maior que o sobrenome")
    print(f"O comprimento do nome é: {len(nome)}")
elif len(nome) == len(sobrenome):
    print("O nome e o sobrenome têm o mesmo comprimento")
    print(f"O comprimento do nome é: {len(nome)}")
    print(f"O comprimento do sobrenome é: {len(sobrenome)}")
else:
    print("O sobrenome é maior que o nome")
    print(f"O comprimento do sobrenome é: {len(sobrenome)}")
#Level 2.6
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
pais = input("Digite seu país: ")
cidade = input("Digite sua cidade: ")
print(f"Nome completo: {nome} {sobrenome}")
print(f"País: {pais}")
print(f"Cidade: {cidade}")

#Level 2.4
num1 = 5
num2 = 4
total = num1 + num2
diferenca = num2 - num1
variavel = num1 * num2
variavel_restante = num1 % num2
exp = num1 ** num2
div_minima = num1 // num2

print("Total:", total)
print("Diferença:", diferenca)
print("Variável:", variavel)
print("Variável Restante:", variavel_restante)
print("Exponenciação:", exp)
print("Divisão Mínima:", div_minima)

#Level 2.5
raio = 30
area = 3 * (raio ** 2)
comprimento = 2 * 3 * raio

print("Área:", area)
print("Comprimento:", comprimento)

help('keywords')

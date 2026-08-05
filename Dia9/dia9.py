idade_usuario = int(input("Digite sua idade: "))#1.1

if (idade_usuario>=18):
    print("Vc pode aprender a dirigir!!!")
elif(idade_usuario<18):
    print(f"Vc precisa de mais {18 - idade_usuario} ano(s) para aprender a dirigir!!!")#1.1

minha_idade = 20 #1.2

sua_idade = int(input("Digite sua idade: "))

if (sua_idade>minha_idade):
    print(f"Vc é mais velho por {sua_idade-minha_idade} ano(s)")
elif(sua_idade<minha_idade):
    print(f"Eu sou mais velho por {minha_idade-sua_idade} ano(s)")
else:
    print("Temos a mesma idade!!!")#1.2

a = int(input("Digite o número A: ")) #1.3
b = int(input("Digite o número B: "))

if(a>b):
    print(f"{a} é maior que {b}")
elif(a<b):
    print(f"{b} é maior que {a}")
else:
    print("Ambos são iguais!!!") #1.3


nota_aluno = int(input("Digite sua Nota(0-100) :")) #2.1

if (0<=nota_aluno<=59):
    print(f"Nota: {nota_aluno}")
    print("Vc tirou F!!!")
elif (60<=nota_aluno<=69):
    print(f"Nota: {nota_aluno}")
    print("Vc tirou D!!!")
elif (69<=nota_aluno<=79):
    print(f"Nota: {nota_aluno}")
    print("Vc tirou C!!!")
elif (79<=nota_aluno<=89):
    print(f"Nota: {nota_aluno}")
    print("Vc tirou B!!!")
elif (89<=nota_aluno<=100):
    print(f"Nota: {nota_aluno}")
    print("Vc tirou A!!!")
else:
    print("Nota inválida")#2.1

mes_ano = input("Digite o mês atual: ").lower()#2.2

if (mes_ano in ("dezembro","janeiro","fevereiro")):
    print("É Inverno!!!")
elif (mes_ano in ("março","abril","maio")):
    print("É Primavera!!!")
elif (mes_ano in ("junho","julho","agosto")):
    print("É Verão!!!")
elif (mes_ano in ("setembro","outubro","novembro")):
    print("É Outono!!!")
else:
    print("Mês Invalido!!!")#2.2

fruits = ['banana', 'laranja', 'manga', 'maçã']#2.3

fruta = input("Digite uma fruta: ")

if (fruta not in fruits):
    fruits.append(fruta)
    print(fruits)
elif (fruta in fruits):
    print("Essa Fruta já existe na lista")#2.3

person={
    'first_name': 'Jadiel',
    'last_name': 'Almeida',
    'age': 20,
    'country': 'Brasil',
    'is_married': "solteiro",
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Álvaro De Andrade',
        'zipcode': '268'
    }
    }

if "skills" in person:
    habilidades = person["skills"]
    meio = len(habilidades)//2
    print(habilidades[meio])
if "skills" in person:
    tem_python = "Python" in person["skills"]
    print(f"Habilidade com Python:{tem_python}")
if "skills" in person:
    front_end = ("JavaScript" and "React") in person["skills"]
    print(f"Trabalha com Front-End: {front_end}")
if "skills" in person:
    back_end = ("Node" and "Python" and "MongoDB") in person["skills"]
    print(f"Trabalha com Back-End: {back_end}")   
if "skills" in person:
    full_stack = ("React" and "Node" and "MongoDb") in person["skills"]
    print(f"Trabalha com Full-Stack: {full_stack}")

if person.get("is_married") == "solteiro" and person.get("country") == "Brasil":
    print(f"{person['first_name']} {person['last_name']} mora no {person['country']}. Ele é Solteiro.")

cachorro = {
   "nome" : "AuAu",
    "cor" : "Branco",
    "perna" : "Comprida",
    "raça" : "Rottweiler",
    "idade" : 10
}#1.1 , 1.2
estudante = {
    "primeiro_nome": "Jadiel",
    "sobrenome": "Almeida Nogueira",
    "gênero": "Masculino",
    "Idade": 20,
    "Status":"Solteiro",
    "Habilidades":["Pcista","Gamer","Python"],
    "País":"Brasil",
    "Cidade":"Fortaleza",
    "Endereço":"Rua Álvaro de Andrade 268"
}#1,3

print(len(estudante))#1.4

print(estudante["Habilidades"])#1.5
print(type(estudante["Habilidades"]))#1.5

estudante["Habilidades"].append("HTML")#1.6
estudante["Habilidades"].append("CSS")#1.6

print(estudante["Habilidades"])

print(estudante.keys())#1.7

print(estudante.values())#1.8

print(estudante.items())#1.9

estudante.pop("Habilidades")#1.10

print(estudante)

del cachorro #1.11
del estudante #1.11
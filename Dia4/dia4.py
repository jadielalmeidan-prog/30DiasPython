#1 e 2

frase1 = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
company = "Coding" + " " + "For" + " " + "All"

#3 a 5
print(frase1)
print(company)
print(len(company))

#6 e 7
print(frase1.upper())#maiusculo
print(company.lower())#minusculo

#8
print(company.capitalize())#primeira letra maiuscula
print(company.title())#cada palavra começa com letra maiuscula
print(company.swapcase())#inverte o caso das letras

#9
print(company[:6])#até a posição 6
print(company[7:])#começa da posição 7 até o final

#10
print(company.index("Coding"))
print(company.find("Coding"))

#11
print(company.replace("Coding", "Python"))#troca a palavra Coding por Python

#12
frase2 = "Python for Everyone"
print(frase2.replace("Everyone", "All"))#troca a palavra Everyone por All

#12+1
print(frase2.split())#divide a string em uma lista de palavras

#12+2
empresas = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(empresas.split(","))#divide a string em uma lista de empresas

#15 a 17
print(company[:1])#1° caractere
print(company[13:15])#Último caractere
print(company[9:11])#10° caractere

#18 e 19
def abbv(frase):
    palavras = frase.split()

    abb = "".join(palavra[0].upper() for palavra in palavras)

    return abb
    #Como fazer Abreviações no python
print(abbv(frase2))
print(abbv(company))

#20
print(company.index("C"))
print(company.index("F"))

#22
company2 = "Coding" + " " + "For" + " " + "All"+ "" + "People"
print(company2.rfind("l"))

#23
frase3 = "You cannot end a sentence with because because because is a conjunction"
print(frase3.find("because"))

#24
print(frase3.rfind("because"))

#25
print(frase3.replace("because",""))#1° forma
#2° forma
resultado = frase3.replace("because because because", "")
resultado = " ".join(resultado.split())
print(resultado)

#28 e 29
print(company.startswith("Coding"))
print(company.endswith("Coding"))

#30
print("   Coding For All     ".strip())

#31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())#True

#33*
print("I am enjoying this challenge.\nI just wonder what is next.")

#34
print("Name\t\t Age\t Country\t City")
print("Asabeneh\t 25\t Finland\t Helsinki")

#35
raio = 10
area = 3 * (raio**2)
print(f"A Área do Circulo com raio {raio} é {area} metros^2")

#36
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} X {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
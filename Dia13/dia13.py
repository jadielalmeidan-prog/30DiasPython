numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativo = [i for i in range(-4,0,1)]
print(negativo)

print("\n")

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
junçao_lists = [i for i in range(1,10,1)]
print(junçao_lists)

print("\n")

lista_de_tuplas = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
for i in lista_de_tuplas:
    print(i)

print("\n")

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises = [(f"País: {p}", f"Cidade: {c}") for sublista in countries for p, c in sublista]
print(paises)

print("\n")

paises_formatados = [[pais.upper(), pais[:3].upper(), cidade.upper()] for sublista in countries for pais, cidade in sublista]
print(paises_formatados)

print("\n")

dict_pais = [{"country": f"{pais.upper()}","city": f"{cidade.upper()}"} for sublista in countries for pais, cidade in sublista]
print(dict_pais)

print("\n")

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nomes = [[f"{nome} {sobrenome}"] for sublista in names for nome,sobrenome in sublista]
print(nomes)

print("\n")

slope = lambda x1,x2,y1,y2 : (x2-x1)/(y2-y1)
print(slope(4,8,2,6))


def soma_dois_numeros(n1,n2):
    print(f"Soma: {n1+n2}")
soma_dois_numeros(6,7)

def area_circulo(raio):
    print(f"Área do Circulo: {3.14 * (raio)**2}")
area_circulo(10)

def soma_entre_numeros(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(soma_entre_numeros(1,2,3))

def conversor_celsius_fahrenheit(C,F):
    F = (C*9)/5 + 32
    print(f"Temperatura em Celsius: {C}")
    print(f"Temperatura em Fahrenheit: {F}") 
conversor_celsius_fahrenheit(100,0)

def check_clima(mes):
    if mes.lower() in ("dezembro","janeiro","fevereiro"):
        print("É Inverno")
    elif mes.lower() in ("março","abril","maio"):
        print("É Primavera")
    elif mes.lower() in ("junho","julho","agosto"):
        print("É Verão")
    elif mes.lower() in ("setembro","outubro","novembro"):
        print("É Outono")
    else:
        print("Mês invalido")
check_clima("Janeiro")

def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 4, 10, 8))

def equacao_quadratica(a,b,c):
    discriminant = (b ** 2) - (4 * a * c)

    root1 = (-b + (discriminant ** 0.5)) / (2 * a)
    root2 = (-b - (discriminant ** 0.5)) / (2 * a)
    
    return root1, root2
print(equacao_quadratica(1,4,3))

def print_list(*items):
    lista = []
    for item in items:
        lista.append(item)
    print (f"{lista}")
print_list("Banana","Maçã","Goiaba")

def reverse_list(*items):
    lista = []
    for item in items:
        lista.append(item)
        lista.reverse()
    print(f"{lista}")
reverse_list("Banana","Maçã","Goiaba")

def capitalize_list_items(lista):
    lista_capitalizada = []
    for item in lista:
        lista_capitalizada.append(item.capitalize())
    return lista_capitalizada

frutas = ['banana', 'laranja', 'manga', 'limão']
print(capitalize_list_items(frutas)) 
    
def add_items(food_stuff,*items):
    food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
    for item in items:
        food_stuff.append(item)
    return food_stuff
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"{food_stuff}")
print(add_items(food_stuff,"Cereal"))

def add_numbers(numbers,*items):
    numbers = [2, 3, 7, 9]
    for item in items:
        numbers.append(item)
    return numbers
numbers = [2, 3, 7, 9]
print(f"{numbers}")
print(add_numbers(numbers,100))

def remove_items(lst,item):
    if item in lst:
        lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"{food_stuff}")
print(remove_items(food_stuff,"Tomato"))

def sum_of_numbers(nums):
    total = 0
    for num in range(nums+1):
        total += num
    return total
print(sum_of_numbers(6))

def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(5))

def sum_of_evens(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_evens(5))

def evens_and_odds(num):
    par = 0
    impar = 0
    for i in range(num + 1):
        if i % 2 == 0:
            par += 1 
        else:
            impar += 1 
    print(f"Pares: {par}")
    print(f"Ímpares: {impar}")
evens_and_odds(100)

import math
def factorial(num):
    print(f"Fatorial de {num}: {math.factorial(num)}")
factorial(4)

def empty(parametro):
    if not parametro:
        return True
    else:
        return False
print(empty(["python"]))
print(empty([]))

def calculate_mean(lista):
    return sum(lista) / len(lista)

def calculate_median(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    if n % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]

def calculate_mode(lista):
    contagem = {}
    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1
    
    max_frequencia = max(contagem.values())
    modas = [k for k, v in contagem.items() if v == max_frequencia]
    return modas

def calculate_range(lista):
    return max(lista) - min(lista)

def calculate_variance(lista):
    media = calculate_mean(lista)
    soma_quadrados = sum((x - media) ** 2 for x in lista)
    return soma_quadrados / len(lista)

def calculate_std(lista):
    variancia = calculate_variance(lista)
    return variancia ** 0.5

def greet(nome = "Guest"):
    print(f"Hello, {nome}!")
greet("Maria")
greet()

def show_args(nome = "Jadiel",idade = 20,cidade= "Fortaleza"):
    print(f"Nome:{nome},Idade: {idade},Cidade: {cidade}")
show_args("Alice",30,"New York")

def primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num /2) + 1):
        if num % i == 0:
            return False
    return True
print(primo(3))
print(primo(1))

def is_unique(lista):
    return len(lista) == len(set(lista))
print(is_unique([2-4]))
print(is_unique([2, 3]))

def is_same_data_type(lista):
    if not lista:
        return True
    primeiro_tipo = type(lista)
    for item in lista:
        if type(item) != primeiro_tipo:
            return False
    return True

print(is_same_data_type(['a', 'b', 1]))
print(is_same_data_type([2-4]))

def is_valid_variable(nome_variavel):
    return nome_variavel.isidentifier()
print(is_valid_variable('minha_variavel'))
print(is_valid_variable('1_variavel'))
print(is_valid_variable('variavel-erro'))
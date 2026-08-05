import random
def random_user_id():
    text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    id = ""
    for i in range(6):
        id += random.choice(text)
    return id
print(random_user_id())

def user_id_gen_by_user(quant,largura):
    text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    id = ""

    quant = int(input("Quantos Id's: "))
    largura = int(input("Quantidade de caracteres: "))

    for i in range(quant):
        for j in range(largura):
            id += random.choice(text)
    return id
print(user_id_gen_by_user(0,0))

def rgb_color_gen():
    n1 = random.randint(0,255)
    n2 = random.randint(0,255)
    n3 = random.randint(0,255)

    print(f"rgb({n1},{n2},{n3})")
rgb_color_gen()

def list_of_hexa_colors():
    caracteres = "0123456789abcdef"
    cor_final = "#"
    for i in range(6):
        cor_final += random.choice(caracteres)
    return cor_final   
print(list_of_hexa_colors())

def list_of_rgb_colors(quant):
    n1 = random.randint(0,255)
    n2 = random.randint(0,255)
    n3 = random.randint(0,255)
    item = f"({n1},{n2},{n3})"
    quant = int(input("Quantidade de cores RGB: "))
    list = []
    for i in range(quant):
        list.append(item)
    print(f"{list}")
list_of_rgb_colors(0)

def generate_colors(tipo, quant):
    lista_cores = []
    caracteres_hex = "0123456789abcdef"
    for _ in range(quant):
        if tipo.lower() == "rgb":
            n1 = random.randint(0, 255)
            n2 = random.randint(0, 255)
            n3 = random.randint(0, 255)
            lista_cores.append(f"rgb({n1},{n2},{n3})")
        elif tipo.lower() == "hexa":
            cor_hex = "#"
            for i in range(6):
                cor_hex += random.choice(caracteres_hex)
            lista_cores.append(cor_hex)
        else:
            return "Tipo Inválido" # Retorno de erro se o tipo não existir
            
    return lista_cores
print(generate_colors("rgb",1))

def shuffle_list(lista):
    return random.sample(lista, len(lista))
frutas = ['banana', 'laranja', 'manga', 'limão']
lista_embaralhada = shuffle_list(frutas)

print(f"Lista original: {frutas}")
print(f"Lista embaralhada: {lista_embaralhada}")

def random_numbers(quant):
    lista = set()
    for i in range(quant):
        item = random.randint(0,9)
        lista.add(item)
    return lista
print(random_numbers(7))


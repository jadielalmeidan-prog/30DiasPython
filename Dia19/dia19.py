def count_linhas(arquivo):
    with open(arquivo,"r") as file:
        linhas = file.readlines()
        return len(linhas)
def count_palavras(arquivo):
    with open(arquivo,"r") as file:
        conteudo = file.read()
        palavras = conteudo.split()
        return len(palavras)
print(f"Linhas no Texto do Trump: {count_linhas("donald_speech.txt")}")
print(f"Palavras no Texto do Trump: {count_palavras("donald_speech.txt")}")
print(f"Linhas no Texto da Melina: {count_linhas("melina_trump_speech.txt")}")
print(f"Palavras no Texto da Melina: {count_palavras("melina_trump_speech.txt")}")
print(f"Linhas no Texto do Obama: {count_linhas("obama_speech.txt")}")
print(f"Palavras no Texto do Obama: {count_palavras("obama_speech.txt")}")
print(f"Linhas no Texto da Michelle: {count_linhas("michelle_obama_speech.txt")}")
print(f"Palavras no Texto da Michelle: {count_palavras("michelle_obama_speech.txt")}")

import json
def most_spoken_languages(arquivo,quant):
    try:
        with open(arquivo,"r",encoding="utf-8") as file:
            data = json.load(file)

            all_languages = []

            for country in data:
                all_languages.extend(country['languages'])
      
            counts = {}
            for lang in all_languages:
                counts[lang] = counts.get(lang, 0) + 1
                formatted_list = [(count, lang) for lang, count in counts.items()]
                formatted_list.sort(reverse=True)

        return formatted_list[:quant]
    except FileNotFoundError:
        return "Erro: O arquivo não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"
print(most_spoken_languages("countries_data.json",3))
print(most_spoken_languages("countries_data.json",10))

def most_populated_countries(arquivo,quant):
    try:
        with open(arquivo,"r",encoding="utf-8") as file:
            data = json.load(file)

            data.sort(key=lambda pais: pais['population'], reverse=True)

            all_population = []

            for pais in data[:quant]:
                all_population.append({
                    'country': pais['name'], 
                    'population': pais['population']
                })
        return all_population     

    except FileNotFoundError:
        return "Erro: O arquivo não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"
print(most_populated_countries("countries_data.json",3))
print(most_populated_countries("countries_data.json",7))

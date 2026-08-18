#No terminal: pip --version

import requests
import json
import statistics
from collections import Counter

def cats():
    try:
        url = "https://api.thecatapi.com/v1/breeds"
        response = requests.get(url) 
        gatos = response.json()

        pesos_medios = []
        idades_medias = []
        paises_origem = []

        for gato in gatos:
            peso_str = gato.get('weight', {}).get('metric', '')
            if ' - ' in peso_str:
                p_min, p_max = [float(p) for p in peso_str.split(' - ')]
                pesos_medios.append((p_min + p_max) / 2)
            
            idade_str = gato.get('life_span', '').replace(' years', '')
            if ' - ' in idade_str:
                i_min, i_max = [float(i) for i in idade_str.split(' - ')]
                idades_medias.append((i_min + i_max) / 2)

            origem = gato.get('origin')
            if origem:
                paises_origem.append(origem)

        def print_stats(nome, dados):
            print(f"\n--- Estatísticas de {nome} ---")
            print(f"Mínimo: {min(dados):.2f}")
            print(f"Máximo: {max(dados):.2f}")
            print(f"Média: {statistics.mean(dados):.2f}")
            print(f"Mediana: {statistics.median(dados):.2f}")
            print(f"Desvio Padrão: {statistics.stdev(dados):.2f}")

        # Resultados de Peso e Vida
        print_stats("Peso (kg)", pesos_medios)
        print_stats("Vida (anos)", idades_medias)

        frequencia_paises = Counter(paises_origem)
        print("\n--- Tabela de Frequência: País vs. Quantidade de Raças ---")
        print(f"{'País':<20} | {'Qtd. Raças'}")
        print("-" * 35)
        for pais, count in frequencia_paises.most_common():
            print(f"{pais:<20} | {count}")
    except Exception as e:
        print(e)
    
cats()

import requests

def analisar_paises_api():
    # URL da API de países (REST Countries v2)
    url = 'https://restcountries.com/v2/all'
    
    try:
        resposta = requests.get(url)
        # Verifica se a requisição foi bem-sucedida
        resposta.raise_for_status()
        
        dados = resposta.json()

        # SEGURANÇA: Garantir que 'dados' seja uma lista antes de processar [1, 4]
        if not isinstance(dados, list):
            print("Erro: A API não retornou uma lista de dados válida.")
            return

        # Filtramos apenas itens que são dicionários para evitar o erro 'str object has no attribute get' [2]
        paises = [p for p in dados if isinstance(p, dict)]

        # 1. Os 10 maiores países por área (Dia 5 - Lists)
        # Usamos .get() de forma segura e tratamos casos onde a área é None
        dez_maiores = sorted(
            paises, 
            key=lambda p: p.get('area') if p.get('area') is not None else 0, 
            reverse=True
        )[:10]

        # 2. As 10 línguas mais faladas (Dia 8 - Dictionaries)
        contagem_linguas = {}
        for p in paises:
            linguas = p.get('languages', [])
            # Verificamos se 'linguas' é de fato uma lista antes de iterar
            if isinstance(linguas, list):
                for l in linguas:
                    if isinstance(l, dict):
                        nome_lingua = l.get('name')
                        if nome_lingua:
                            contagem_linguas[nome_lingua] = contagem_linguas.get(nome_lingua, 0) + 1

        linguas_mais_faladas = sorted(
            contagem_linguas.items(), 
            key=lambda x: x[5], 
            reverse=True
        )[:10]

        # 3. Número total de línguas únicas (Dia 7 - Sets)
        total_linguas = len(contagem_linguas)

        # Exibição dos Resultados
        print("--- 10 Maiores Países (Área) ---")
        for i, p in enumerate(dez_maiores, 1):
            print(f"{i}. {p.get('name')} - {p.get('area')} km²")

        print("\n--- 10 Línguas Mais Faladas (por número de países) ---")
        for i, (lingua, qtd) in enumerate(linguas_mais_faladas, 1):
            print(f"{i}. {lingua}: {qtd} países")

        print(f"\nTotal de línguas únicas na API: {total_linguas}")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        # Tratamento de exceção genérico para debugging (Dia 1 e 17) [1]
        print(f"Ocorreu um erro inesperado: {e}")

analisar_paises_api()
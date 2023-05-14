import argparse
import re

# Configuração do parser de argumentos
parser = argparse.ArgumentParser(description='Extrai os parâmetros presentes em uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo de texto contendo a lista de URLs.')

# Função que extrai os parâmetros de uma URL
def extrair_parametros(url):
    # Expressão regular para encontrar todos os parâmetros presentes na URL
    padrao = r'\?(.*?)(&|$)'
    # Encontra todos os parâmetros e adiciona em uma lista
    parametros = re.findall(padrao, url)
    # Retorna a lista de parâmetros
    return parametros

# Função principal
def main():
    # Faz o parsing dos argumentos
    args = parser.parse_args()
    # Lê o arquivo de texto com a lista de URLs
    with open(args.lista, 'r') as arquivo:
        urls = arquivo.read().splitlines()
    # Extrai e exibe os parâmetros de cada URL
    lista_parametros = []
    for url in urls:
        parametros = extrair_parametros(url)
        if parametros:
            for parametro in parametros:
                lista_parametros.append(parametro[0].split('=')[0])
    # Exibe a lista final sem repetição
    lista_parametros_sem_repeticao = list(set(lista_parametros))
    for parametro in lista_parametros_sem_repeticao:
        print(parametro)

if __name__ == '__main__':
    main()

import argparse
import re

parser = argparse.ArgumentParser(description='Extrai os parâmetros presentes em uma lista de URLs.')
parser.add_argument('-l', '--lista', type=str, help='Arquivo de texto contendo a lista de URLs.')

def extrair_parametros(url):
    padrao = r'\?(.*?)(&|$)'
    parametros = re.findall(padrao, url)
    return parametros

def main():
    args = parser.parse_args()
    with open(args.lista, 'r') as arquivo:
        urls = arquivo.read().splitlines()
    lista_parametros = []
    for url in urls:
        parametros = extrair_parametros(url)
        if parametros:
            for parametro in parametros:
                lista_parametros.append(parametro[0].split('=')[0])
    lista_parametros_sem_repeticao = list(set(lista_parametros))
    for parametro in lista_parametros_sem_repeticao:
        print(parametro)

if __name__ == '__main__':
    main()

import os

def limparTela():
    os.system ("cls")

def lerPalavra(tamanho):    
    tamanhoPalavra = len(tamanho)
    return tamanhoPalavra

def convertePalavra(palavra):
    palavra.upper()
    return palavra

def pulaLinha():
    print("\n")

def anotaVencedor(arquivo, valor):
    with open("arquivo") as a:
        a.write(str(valor) + "\n")


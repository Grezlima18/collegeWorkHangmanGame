from funcoes import limparTela, lerPalavra

competidor=input("Insira o nome do competidor:")
desafiante=input("insira o nome do desafiante:")
limparTela()

palavra=input("Desafiante insira a palavra chave: ")

tamanhoPalavra=lerPalavra(palavra)

todasAsDicas = []

dica1 = input("Desafiante insira a primeira dica: ")
todasAsDicas.append(dica1)
dica2 = input("Desafiante insira a segunda dica: ")
todasAsDicas.append(dica2)
dica3 = input("Desafiante insira a terceira dica: ")
todasAsDicas.append(dica3)

print(todasAsDicas)
input()
limparTela()

converteAsterisco = tamanhoPalavra * "*"
print(converteAsterisco)

while True:
    print("{}, qual opção deseja realizar?" .format(competidor))
    print("> Digite 1 para solicitar uma dica!")
    print("> Digite 2 para chutar uma letra!")
    escolha = input()
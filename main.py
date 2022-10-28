from funcoes import limparTela, lerPalavra

competidor=input("Insira o nome do competidor: ")
desafiante=input("insira o nome do desafiante: ")
limparTela()

palavra=input("Desafiante insira a palavra chave: ")

todasAsDicas = []

tamanhoPalavra=lerPalavra(palavra)

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
print("Quantidade de digitos da palavra:")
print(converteAsterisco)


tentativas = 0
while True:
    print("{}, qual opção deseja realizar?" .format(competidor))
    print("> Digite 1 para solicitar uma dica!")
    print("> Digite 2 para chutar uma letra!")
    try:
        escolha = int(input())
        if escolha == 1:
            if tentativas == 0:
                print("Sua primeira dica é:", dica1)
                tentativas += 1
            elif tentativas == 1:
                print ("Sua segunda dica é:", dica2)
                tentativas += 1
            elif tentativas == 2:
                print("Sua terceira e última dica é:", dica3)
                tentativas += 1
            else:
                print("Você não tem mais direito a dicas!")
        elif escolha == 2:
            print("Certo, qual letra você escolhe?")
            input()
            break
        else:
            error
    except:
        print("Numero invalido!")

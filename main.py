from funcoes import limparTela, lerPalavra, convertePalavra

competidor=input("Insira o nome do competidor: ")
desafiante=input("insira o nome do desafiante: ")
limparTela()

palavra=input("Desafiante insira a palavra chave: ").upper()
convertePalavra(palavra)

tamanhoPalavra=lerPalavra(palavra)

todasAsDicas = []

dica1 = input("Desafiante insira a primeira dica: ")
todasAsDicas.append(dica1)
dica2 = input("Desafiante insira a segunda dica: ")
todasAsDicas.append(dica2)
dica3 = input("Desafiante insira a terceira dica: ")
todasAsDicas.append(dica3)

limparTela()

palavraEmAsterisco = []

for i in range(0,tamanhoPalavra):
    palavraEmAsterisco.append("*")

totalDeDicas = 0
totalDeTentativas = 6

while True:
    print("Palavra escolhida pelo {}:" .format(desafiante))
    print(palavraEmAsterisco)
    print("{}, qual opção deseja realizar?" .format(competidor))
    print("> Digite 1 para solicitar uma dica!")
    print("> Digite 2 para chutar uma letra!")
    print("> Digite 3 para começar novamente!")
    
    try:
        escolha = int(input())

        if escolha == 1:
            if totalDeDicas == 0:
                print("Sua primeira dica é:", todasAsDicas[0])
                totalDeDicas += 1
            
            elif totalDeDicas == 1:
                print ("Sua segunda dica é:", todasAsDicas[1])
                totalDeDicas  += 1
            
            elif totalDeDicas == 2:
                print("Sua terceira e última dica é:", todasAsDicas[2])
                totalDeDicas += 1
            
            else:
                print("Você não tem mais direito a dicas!")
        
        
        elif escolha == 2:
            letrasChutas = []
            print("Certo, qual letra você escolhe?")
            print("Você ainda tem {} tentativas" .format(totalDeTentativas))
            letraEscolhida = input(">> ").upper()
            letrasChutas.append(letraEscolhida)

            if letraEscolhida in palavra and len(letraEscolhida) == 1:
                posicaoDaLetraCerta = palavra.index(letraEscolhida)
                palavraEmAsterisco[posicaoDaLetraCerta] = letraEscolhida

            elif letraEscolhida not in palavra and len(letraEscolhida) == 1:
                totalDeTentativas -= 1
                print("Você errou! Restam apenas {} tentativas" .format(totalDeTentativas))
                
                if totalDeTentativas == 0:
                    print("{} venceu a partida! A palavra era {}" .format(desafiante, palavra))
                    break
            
            else:
                print("Somente é aceito letras! Não é possível chutar a palavra ou digitar mais de uma letra por vez!")
            


        elif escolha == 3:
            break

        else:
            error
    
    except:
        print("somente será aceito o número 1 e 2!")

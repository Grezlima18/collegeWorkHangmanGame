from funcoes import limparTela, lerPalavra, convertePalavra, pulaLinha, anotaVencedor

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
letrasErradas = []
palavrasErradas = []

for i in range(0,tamanhoPalavra):
    palavraEmAsterisco.append("*")

totalDeDicas = 0
totalDeTentativas = 6

while True:
    if totalDeTentativas == 0:
        break

    if palavraEmAsterisco == list(palavra):
        print("Parabéns! {} descobriu a palavra e venceu o jogo!" .format(competidor))
        f = open("vencedores.txt", "a")
        f.write("\nPalavra: {} – Vencedor: Competidor {}, Perdedor: Desafiante {}".format(palavra,competidor, desafiante))
        f.close()
        break

    pulaLinha()
    print(palavraEmAsterisco)
    pulaLinha()
    print("{}, qual opção deseja realizar?" .format(competidor))
    print("> Digite 1 para solicitar uma DICA!")
    print("> Digite 2 para chutar uma LETRA!")
    print("> Digite 3 para chuta a PALAVRA!")
    print("> Digite 4 SAIR do jogo!")

    try:
        escolha = int(input())
        pulaLinha()

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
                print("Suas dicas foram: {}, {}, {}" .format(todasAsDicas[0], todasAsDicas[1], todasAsDicas[2]))
                print("Você não tem mais direito a dicas!")
        
        
        elif escolha == 2:
            letrasChutadas = []
            print("Certo, qual letra você escolhe?")
            print("Você ainda tem {} tentativas" .format(totalDeTentativas))
            letraEscolhida = input(">> ").upper()
            letrasChutadas.append(letraEscolhida)

            if letraEscolhida in palavra and len(letraEscolhida) == 1:
                posicaoDaLetraCerta = [i for i,val in enumerate(palavra) if val==letraEscolhida]
                contador = 0

                if letraEscolhida in palavraEmAsterisco:
                    print("Você já chutou essa letra! Insira uma letra não utilizada!")

                while contador < len(posicaoDaLetraCerta):
                    palavraEmAsterisco[posicaoDaLetraCerta[contador]] = letraEscolhida
                    contador += 1

            elif letraEscolhida not in palavra and len(letraEscolhida) == 1:
                if letraEscolhida in letrasErradas:
                    print("Você já chutou essa letra! Insira uma letra não utilizada!")
                    
                else:
                    letrasErradas.append(letraEscolhida)
                    totalDeTentativas -= 1
                    print("Você errou! Restam apenas {} tentativas" .format(totalDeTentativas))
                
                if totalDeTentativas == 0:
                    print("{} venceu a partida! A palavra era {}" .format(desafiante, palavra))
                    f = open("vencedores.txt", "a")
                    f.write("\nPalavra: {} – Vencedor: Desafiante {}, Perdedor: Competidor {}".format(palavra, desafiante, competidor))
                    f.close()
                    break

            else:
                print("Somente é aceito letras! Não é possível chutar a palavra ou digitar mais de uma letra por vez!")

        elif escolha == 3:
            palpite = input("Insira a palavra: ").upper()

            if palpite == palavra:
                print("Parabéns! {} descobriu a palavra e venceu o jogo!" .format(competidor))
                f = open("vencedores.txt", "a")
                f.write("\nPalavra: {} – Vencedor: Competidor {}, Perdedor: Desafiante {}".format(palavra,competidor, desafiante))
                f.close()
                break

            else:
                while True:
                    if palpite not in palavrasErradas:
                        palavrasErradas.append(palpite)
                        totalDeTentativas -= 1
                        print("Você errou! Restam apenas {} tentativas" .format(totalDeTentativas))
                        break

                    else:
                        print("Você já chutou essa palavra! Insira outra que não tenha utilizado!")
                        palpite = input("Insira a palavra: ").upper()

                        if palpite == palavra:
                            palavraEmAsterisco = list(palavra)
                            break


        elif escolha == 4:
            break

        else:
            error
    
    except:
        print("somente será aceito o número 1 e 2!")
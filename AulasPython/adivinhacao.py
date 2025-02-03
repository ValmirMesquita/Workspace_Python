import random



def jogar():
    print("*********************************")
    print("Bem vindo ao jogo do Adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil  (2) Médio  (3) Dificil")

    nivel = int(input("Defina o nivel do Jogo!"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")

        chute_str = input("Digite um numero de 1 a 100:")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos}")
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Você errou O seu chute foi menor que o numero secreto")
            pontos_perdidos = (numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Game Ouver")


if __name__ == '__main__':
    jogar()

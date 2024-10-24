import random


def jogo_de_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    while True:
        numero_digitado = int(input("Digite um número entre 1 e 100: "))
        if numero_digitado < numero_aleatorio:
            print("O número é maior. Tente novamente.")
        elif numero_digitado > numero_aleatorio:
            print("O número é menor. Tente novamente.")
        else:
            print("Parabéns! Você acertou o número.")
            break


jogo_de_adivinhacao()

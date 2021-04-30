import random

print("********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("********************************")

secret_number = random.random() * 100

kick = 0

while secret_number != kick:
    kick = int(input("Digite seu número"))

    print("Você digitou: ", kick)

    if secret_number == kick:
        print("Você acertou!")
    else:
        print("Você errou!")

        if kick > secret_number:
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif kick < secret_number:
            print("Você errou! O seu chute foi menor do que o número secreto!")

print ("Fim de jogo")


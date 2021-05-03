import random


def play():
    printApresentation()

    secret_word = loadSecretWord()

    correct_leters = initializeCorrectWods(secret_word)
    print(correct_leters)

    hanged = False
    correct = False
    errors = 0

    while not hanged and not correct:
        kick = input("Qual a letra?: ").strip().upper()

        if kick in secret_word:
            markCorrectKick(kick, correct_leters, secret_word)
        else:
            errors += 1
            drawHanged(errors)
        hanged = errors == 7
        correct = "_" not in correct_leters
        print(correct_leters)

    if correct:
        print("Você ganhou! A palavra secreta era: ", secret_word)
    else:
        print("Você perdeu! A palavra secreta era: ", secret_word)

    print("Fim de jogo!")


def printApresentation():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def loadSecretWord():
    archive = open("words.txt", "r")
    words = []
    for line in archive:
        words.append(line.strip())

    archive.close()

    idx = random.randrange(0, len(words))

    return words[idx].upper()


def initializeCorrectWods(word):
    return ["_" for leter in word]


def markCorrectKick(kick, correct_leters, secret_word):
    idx = 0
    for leter in secret_word:
        if kick == leter:
            correct_leters[idx] = leter
        idx += 1

def drawHanged(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if __name__ == "__main__":
    play()

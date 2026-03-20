from random import randint

player = int(input("Escreva um número de 0 a 5: "))
computador = randint(0,5)
print("PLAYER: ", player)
print("COMPUTADOR: ", computador)

if player == computador:
    print("O jogador venceu!")
else:
    print("O computador venceu!")

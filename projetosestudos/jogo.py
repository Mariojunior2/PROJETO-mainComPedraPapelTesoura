from random import randint

choice = ["pedra","papel","tesoura"]

computer = choice[randint(0,2)]

print("Bem Vindo! Ao meu jogo de pedra,papel e tesoura\n")
jogador = input("Fale Pedra,Papel ou tesoura: ").lower()


if jogador == computer:
    print("Computador Escolheu: " + computer)
    print("Empatou")
elif jogador == "pedra" and computer == "papel":
    print("Computador Escolheu: " + computer)
    print("Maquina Te Solou Gostoso")
elif jogador == "papel" and computer == "tesoura":
    print("Computador Escolheu: " + computer)
    print("Maquina Te Solou Gostoso")
elif jogador == "tesoura" and computer == "pedra":
    print("Computador Escolheu: " + computer)
    print("Maquina Te Solou Gostoso")
elif jogador == "papel" and computer == "pedra":
    print("Computador Escolheu: " + computer)
    print("Você Solou a maquina GOSTOSO")
elif jogador == "tesoura" and computer == "papel":
     print("Computador Escolheu: " + computer)
     print("Você Solou a maquina GOSTOSO")
elif jogador == "pedra" and computer == "tesoura":
     print("Computador Escolheu: " + computer)
     print("Você Solou a maquina GOSTOSO")
else:
    print("Inseria um valor válido")

from random import randint

choice = ["pedra","papel","tesoura"]

computer = choice[randint(0,2)]

print("Bem Vindo! Ao meu jogo de pedra,papel e tesoura\n")
jogador = input("Fale Pedra,Papel ou tesoura: ").lower()


if jogador == computer:
    print("Você Escolheu: \n" + jogador.capitalize())
    print("Computador Escolheu: \n" + computer)
    print("Empatou")
elif jogador == "pedra" and computer == "papel":
    print("Você Escolheu: \n" + jogador.capitalize())
    print("Computador Escolheu: \n" + computer.capitalize())
    print("Maquina Te Solou Gostoso")
elif jogador == "papel" and computer == "tesoura":
    print("Você Escolheu: \n" + jogador.capitalize())
    print("Computador Escolheu: \n" + computer.capitalize())
    print("Maquina Te Solou Gostoso")
elif jogador == "tesoura" and computer == "pedra":
    print("Você Escolheu: \n" + jogador.capitalize())
    print("Computador Escolheu: \n" + computer.capitalize())
    print("Maquina Te Solou Gostoso \n")
elif jogador == "papel" and computer == "pedra":
    print("Você Escolheu: \n" + jogador.capitalize())
    print("Computador Escolheu: \n" + computer.capitalize())
    print("Você Solou a maquina GOSTOSO")
elif jogador == "tesoura" and computer == "papel":
     print("Você Escolheu: \n" + jogador.capitalize())
     print("Computador Escolheu: \n" + computer.capitalize())
     print("Você Solou a maquina GOSTOSO")
elif jogador == "pedra" and computer == "tesoura":
     print("Você Escolheu: \n" + jogador.capitalize())
     print("Computador Escolheu: \n" + computer.capitalize())
     print("Você Solou a maquina GOSTOSO")
else:
    print("Inseria um valor válido \n")

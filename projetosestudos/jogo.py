from random import randint

choice = ["pedra","papel","tesoura"]

computer = choice[randint(0,2)]

print("Bem Vindo! Ao meu jogo de pedra,papel e tesoura\n")
jogador = input("Fale Pedra,Papel ou tesoura: ").lower()


if jogador == computer:
    print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Empatou")
elif jogador == "pedra" and computer == "papel": # AND serve para espécificar mais uma condição
    print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Maquina Te Solou Gostoso")
elif jogador == "papel" and computer == "tesoura": # AND serve para espécificar mais uma condição
    print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Maquina Te Solou Gostoso")
elif jogador == "tesoura" and computer == "pedra": # AND serve para espécificar mais uma condição
    print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Maquina Te Solou Gostoso \n")
elif jogador == "papel" and computer == "pedra": # AND serve para espécificar mais uma condição
    print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
    print("Você Solou a maquina GOSTOSO")
elif jogador == "tesoura" and computer == "papel": # AND serve para espécificar mais uma condição
     print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
     print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
     print("Você Solou a maquina GOSTOSO")
elif jogador == "pedra" and computer == "tesoura": # AND serve para espécificar mais uma condição
     print("Você Escolheu: \n" + jogador.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
     print("Computador Escolheu: \n" + computer.capitalize()) # CAPITALIZE DEIXA A PRIMEIRA LETRA MAINSCULA
     print("Você Solou a maquina GOSTOSO")
else:
    print("Inseria um valor válido \n")

import random

numero_secreto = random.randint(1, 10)

tentativas = 0
max_tentativas = 10

while tentativas < max_tentativas:
    palpite = int(input("Adivinhe o number entre 1 e 10: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print("Parabens Acertou")
        tentativas += 10
    elif palpite < numero_secreto:
        print("Tente um Number maior")
    else:
        print("Tente um number menor")
else:
    print("O number era", numero_secreto)
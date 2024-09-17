# Calculadora Base para treino com NUMBERS

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (+, -, *, /, **, %): ")

resultado = None
erro = None

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '**':
    resultado = numero1 ** numero2
elif operador == '%':
    resultado = numero1 % numero2
elif operador == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        erro = "Erro: Dividir por zero!"
else:
    erro = "Operador nao presente tente novamente!"

if erro:
    print(erro)
else:
    print("Resultado: ", resultado)
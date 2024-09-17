# Todos os operadores
# Metod seria Metodo

soma = 10 + 5 # Resultado 15 Metod Soma

diferenca = 10 - 5 # Resultado 5 Metod Diminuir

produto = 10 * 5 # Resultado 50 Metod Multiplicar

quociente = 10 / 5 # Resultado 2.0 divisao

potencia = 2 ** 3 # Resultado 8 Metod Elevado


Iguala = '=='

deferentde = '!='

maiorque = '>'

menorque = '<'

maiorouigual = '>='

menorigual = '<='

# AND:  Retorna True se ambas as condições forem verdadeiras.
# OR: Retorna True se pelos menos uma for verdadeira
# NOT: inverte a logica da condicao

idade = 20
habilitacao = True

if idade >= 18 and habilitacao:
    print("Pode dirigir.")
else:
    print("Nao pode dirigir.")


# Maior que (>), Menor que (<), Igual a (==), Diferente de (!=), Maior ou igual a (>=), Menor ou igual a (<=).

WHILE = 'condicao executa se for verdadeiro'
contador = 0
while contador < 10:
    print("Contado", contador)
    contador += 1 # Equivale a contador = contador + 1
    
FOR = 'Faz uma sequencia como uma lista,tupla ou string'
# EXEMPLO 'for variavel in sequencia:'
# EXEMPLO COM STRINGS
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print("Eu goto de", fruta)
# EXEMPLO COM NUMBER
for i in range(10):
    print("Number: ", i) 

# Exemplo de Controle de Fluxo 'BREAK'
for num in range(10):
    if num == 5:
        break
    print(num)

# EXEMPLO com pular para a poxima

for nume in range(10):
    if nume == 2:
        continue
    print(nume)

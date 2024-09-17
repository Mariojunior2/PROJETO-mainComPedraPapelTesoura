if condição:  # type: ignore 
# executada o condigo so se for verdadeiro
# exemplo 
    idade = 18
if idade >= 18:
    print("De maior")
elif idade <= 18: # Executa o elif se a condicao anterior for falsa
    print("De menor")    
else: # Executa se um bloco de codigo for falso
    print("Errado tente por um valor bom")
    
    
nota = 85

if nota >= 90:
    conceito = 'A+'
elif nota >= 80:
    conceito = 'A'
elif nota >= 70:
    conceito = 'IN'
elif nota >= 60:
    conceito = 'INV'
else:
    conceito = 'INVF'

print("Seu conceito ser", conceito)
    
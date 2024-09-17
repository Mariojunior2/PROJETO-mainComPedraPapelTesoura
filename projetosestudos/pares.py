print("Me fale dois numeros que farei seus pares! ")


In = int(input("Me fale o numero inical "))
IIn = int(input("Me fale o segundo final "))
if IIn <= In:
    print("Tente Novamente")

 
for i in range(In, IIn):
    if i % 2 == 0:
        print(i + 2)
    
        
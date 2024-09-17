def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = (-b + D**(1/2)) / (2*a)
    x2 = (-b - D**(1/2)) / (2*a)
    
    Dex = (-b) / (2*a)
    DeY = (- D) / (4*a)
    
    print('Valor de x1: {0}'.format(x1))
    print('Valor de x2:{0}'.format(x2))
    print((Dex))
    print((DeY))
    
if __name__ == '__main__':
    while True:
        print('Calculando raizes de uma de 2*grau sklsksk')
        a = float(input('Valor de a: '))
        b = float(input('Valor de b: '))
        c = float(input('Valor de c: '))
        raizes(a,b,c)
        
        continua = input('Deseja sair? Digete a ou Enter para cálculo:')
        if (continua == 'a'):
            break
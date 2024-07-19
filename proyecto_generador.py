def mi_generadorFarmacia():
    for x in range(0,1000):
        x=x + 1
        yield f'F-{x}'


def mi_generadorPerfumeria():
    for x in range(0,1000):
        x=x + 1
        yield f'P-{x}'


def mi_generadorCosmetica():
    for x in range(0,1000):
        x=x + 1
        yield f'C-{x}'


f= mi_generadorFarmacia()
p= mi_generadorPerfumeria()
c= mi_generadorCosmetica()


def decorar_saludo(rubro):                  #si el usuario pone un P, imprimira el generador p, asi mismo con los demas

    print('\n' + '*' * 23)
    print('Su numero es: ')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print('Aguarde y sera atendido')
    print('*' * 23 + '\n')





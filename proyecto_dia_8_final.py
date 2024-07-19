import proyecto_generador


def preguntar():
    print('¡¡Bienvenido a Farmacia Pyhton!!')

    while True:
        print(' [P] Perfumería\n [F] Farmacia\n [C] Cosmética')

        try:
            mi_rubro= input('Elige una categoria: ').upper()
            ['P','F','C'].index(mi_rubro)                       #esta linea se encarga de buscar si la respuesta del usuario es uno de estos valores o no

        except ValueError:
            print('\nEsa no es un opción válida')

        else:
            break               #Hace que que salga del loop y se mete en el loop donde se le pregunata si quiere otro numero

    proyecto_generador.decorar_saludo(mi_rubro)                #aqui se pasa la letra de 'mi_rubro' a la funcion decorar saludo


def inicio():
    while True:
        preguntar()
        try:
            otro_turno= input('Quieres sacar otro turno? [S] [N]').upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opción válida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break


inicio()



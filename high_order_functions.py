def run():
    hola = lambda: print('Hola')
    adios = lambda: print('Adios')
    saludo = lambda func: func()

    saludo(hola)
    saludo(adios)


if __name__ == '__main__':
    run()
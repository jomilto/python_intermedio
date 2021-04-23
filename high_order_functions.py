def run():
    hola = lambda: print('Hola')
    adios = lambda: print('Adios')
    saludo = lambda func: func()

    saludo(hola)

    numbers = [ i for i in range(1,50)]
    odds = list(filter(lambda x: x % 2 != 0, numbers))

    print(odds)

    saludo(adios)

if __name__ == '__main__':
    run()
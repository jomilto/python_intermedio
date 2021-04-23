def run():
    hola = lambda: print('Hola')
    adios = lambda: print('Adios')
    saludo = lambda func: func()

    saludo(hola)

    numbers = [ i for i in range(1,50)]
    odds = list(filter(lambda x: x % 2 != 0, numbers))

    squares = list(map(lambda x: x**2,numbers))

    print(odds)
    print(squares)

    saludo(adios)

if __name__ == '__main__':
    run()
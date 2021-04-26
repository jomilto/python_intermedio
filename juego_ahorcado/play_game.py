from random import randint

def get_data_options():
    data = []
    with open('../archivos/data.txt','r',encoding='utf-8') as f:
        data = [ line for line in f]

    return data

def get_palabra():
    data = get_data_options()
    number = randint(1,len(data))
    return data[number].upper().replace('\n','')

def start_game():
    mensaje ="""
Bienvenido al juego del ahorcado. :D
Adivina la palabra antes de que otro pobre hombre de bits termine colgado. :'(

Buena suerte!!! :)
    """
    print(mensaje)

def print_ahorcado(user_errors):
    ahorcado = [
        """
             |------
             |
             |
             |
        _____|______
        """,
        """
             |------|
             |
             |
             |
        _____|______
        """,
        """
             |------|
             |      O
             |
             |
        _____|______
        """,
        """
             |------|
             |      O
             |      |
             |
        _____|______
        """,
        """
             |------|
             |      O
             |     /|
             |
        _____|______
        """,
        """
             |------|
             |      O
             |     /|\\
             |
        _____|______
        """,  
        """
             |------|
             |      O
             |     /|\\
             |     /
        _____|______
        """,  
        """
             |------|
             |      O
             |     /|\\   Game Over!!! :'(
             |     / \\
        _____|______
        """,           
    ]
    print(ahorcado[user_errors])

def check(correct, palabra, caracter, user_errors):
    found = 0
    for i in range(0,len(palabra)):
        if palabra[i] == caracter:
            correct[i] = caracter
            found+=1
    
    if found == 0:
        user_errors+=1
        print_ahorcado(user_errors)

    return correct, user_errors

def print_arreglo(arreglo):
    cadena = ''
    for letter in arreglo:
        cadena = cadena + letter + ' '

    print(cadena)
    
def run():
    caracter = ''
    winner = False
    start_game()
    palabra = [ letter for letter in get_palabra() ]
    user_errors = 0
    correct = ['_' for i in range(1,len(palabra)+1)]
    print_ahorcado(user_errors)
    print_arreglo(correct)
    while (len(caracter) == 0 and winner == False and user_errors < 7):
        caracter = input('Ingresa una letra: ')
        if caracter.isnumeric():
            caracter = ''
        else:
            correct, user_errors = check(correct,palabra,caracter.upper(), user_errors)
            caracter = ''
            print_arreglo(correct)
            if correct == palabra:
                winner = True
                print('Ganaste')
if __name__ == '__main__':
    run()
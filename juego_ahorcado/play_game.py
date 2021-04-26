from random import choice

AHORCADO = [
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

def get_palabra():
    data = []
    with open('../archivos/data.txt','r',encoding='utf-8') as f:
        data = [ line for line in f]
    palabra = choice(data)

    return palabra.upper().replace('\n','')

def start_game(palabra):
    mensaje ="""
Bienvenido al juego del ahorcado. :D
Adivina la palabra antes de que otro pobre hombre de bits termine colgado. :'(

Buena suerte!!! :)
    """
    print(mensaje)
    print('La palabra tiene ',len(palabra),' caracteres')

def print_ahorcado(user_errors):
    print(AHORCADO[user_errors])

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
    # cadena = ''
    # for letter in arreglo:
    #     cadena = cadena + letter + ' '

    print(*arreglo)
    
def run():
    caracter = ''
    winner = False
    palabra = [ letter for letter in get_palabra() ]
    start_game(palabra)
    user_errors = 0
    correct = ['_' for i in range(1,len(palabra)+1)]
    print_ahorcado(user_errors)
    print_arreglo(correct)
    while (len(caracter) == 0 and winner == False and user_errors < len(AHORCADO)-1):
        caracter = input('Ingresa una letra: ')
        if caracter.isnumeric() or len(caracter) == 0:
            caracter = ''
        else:
            correct, user_errors = check(correct,palabra,caracter.upper(), user_errors)
            caracter = ''
            print_arreglo(correct)
            if correct == palabra:
                winner = True
                print('Ganaste :D')
    if user_errors == 7:
        print('La palabra era ', ''.join(palabra))
if __name__ == '__main__':
    run()
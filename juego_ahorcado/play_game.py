from random import randint

def get_data_options():
    data = []
    with open('../archivos/data.txt','r',encoding='utf-8') as f:
        data = [ line for line in f]

    return data

def get_palabra():
    data = get_data_options()
    number = randint(1,len(data))
    return data[number]

def start_game():
    mensaje ="""
Bienvenido al juego del ahorcado. :D
Adivina la palabra antes de que otro pobre hombre de bits termine colgado. :'(

Buena suerte!!! :)
    """
    print(mensaje)

def check():
    pass
    
def run():
    caracter = ''
    start_game()
    palabra = get_palabra()
    user_tries = 0
    correct = ['_' for i in range(1,len(palabra)+1)]
    while len(caracter) == 0:
        caracter = input('Ingresa una letra: ')
        if caracter.isnumeric():
            caracter = ''
        else:
            check()

if __name__ == '__main__':
    run()
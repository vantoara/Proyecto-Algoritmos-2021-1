from Player import Player
from Guessing import Guessing
from Word_Search import Word_Search
from Crypto import Crypto
from Hangman import Hangman
from Math import Math
import requests
import random
import enquiries

def validate_password():
    while True:
        password = input("Ingrese su nueva contraseña: ")
        if len(password) < 8:
            print("La contraseña elegida no es válida.")
        else:
            #Los any iteran a través de los varios for loops y si UN solo caracter cumple la condición (regresa True) entonces, la condición regresará True, por  ende, utilicé varios any (varios for loop idénticos) para ver que las condiciones de la contraseña se cumplan.
            if any(character.isspace() for character in password):
                print("La contraseña elegida no es válida.")
            else:
                if (not any(character.isdigit() for character in password)) or (not any(character.isalpha() for character in password)):
                    print("La contraseña elegida no es válida.")
                else:
                    if any(character.islower() for character in password) and any(character.isupper() for character in password):
                        if any(not character.isalnum() for character in password):
                            print("Contraseña ingresada correctamente")
                            break
                        else:
                            print("La contraseña elegida no es válida.")
                    else:
                        print("La contraseña elegida no es válida.")

def registry(database):
    user = input("\nIngrese su nombre de usuario: ")
    if user in database:
        print("\nIngreso inválido, usuario ya registrado.")
    while len(user) < 3 and len(user) > 8:
        print("\nNombre de usuario es muy largo o muy corto. Debe de ser entre 3 y 8 caracteres.")
        user = input("\nIngrese su nombre de usuario: ")
    password = validate_password()
    age = input("\nIngrese su edad: ")
    while not age.isdigit() or int(age) < 16:
        print("Edad es inválida. Recuerde que debe ser mayor de 16 años para poder jugar.")
        age = input("\nIngrese su edad: ")
    player = Player(user, password, int(age))
    database.append(player)
    return player


#   avatars = ["Scharifker", "Eugenio Mendoza", "Pelusa", "Gandhi", "Metropavo", "Exodia", "Lorenzo Mendoza", "Becado"]

room = 1
obj = 1

def guessing_game():

    game = Guessing(room, obj)
    game.show_game()
    game.show_question()

    while True:

        option = input("\nEscoja una opción:\n1. Responder\n2. Pista\n--> ")
        while not option.isdigit() or int(option) not in range (1,3):
            option = input("\nEscoja una opción:\n1. Responder\n2. Pista\n--> ")

        if option == "1":
            player_guess = input("Ingrese su respuesta: ")
            answer = game.guess(player_guess)
            if answer == True:
                break
                #añadir rencompensa
            #else:
                #pierdes vida y F

        else:
            game.get_clue()

def word_search_game():

    game = Word_Search(room, obj)
    game.show_game()
    game.show_soup()

    while True:

        option = input("\nEscoja una opción: \n1. Responder\n2. Pista\n--> ")
        while not option.isdigit() or int(option) not in range (1,3):
            option = input("\nEscoja una opción:\n1. Responder\n2. Pista\n--> ")

        if option == "1":
            player_guess = (input("Ingrese su respuesta: ")).lower()
            answer = game.guess_word(player_guess)
            if answer == True:
                pass
                #añadir rencompensa
            #else:
                #pierdes vida y F

        else:
            game.get_word_clue()

def cryptic_game():

    game = Crypto(room, obj)
    game.show_game()
    game.show_alphabet()
    game.show_encode()

    player_decode = (input("\nDescrife el código e ingrese su respuesta: ")).lower()

    answer = game.answer_decode(player_decode)
    if answer == True:
        pass
        #añadir rencompensa
    #else:
        #pierdes vida y F

def hangman_game():

    game = Hangman(room, obj)
    game.show_game()
    game.show_prompt()

    while True:
        option = input("\nEscoja una opción: \n1. Adivinar una (1) letra\n2. Pista\n--> ")
        while not option.isdigit() or int(option) not in range (1,3):
            option = input("\nEscoja una opción:\n1. Adivinar una (1) letra\n2. Pista\n--> ")
        if option == "1":
            player_letter = (input("Ingrese una letra: ")).lower()
            while not player_letter.isalpha():
                print("Entrada inválida. Por favor, ingrese una letra.")
                player_letter = (input("Ingrese una letra: ")).lower()
            answer = game.guess_hangman(player_letter)
            if answer == True:
                break
                    #añadir rencompensa
            elif answer == False:
                break
        else:
            game.get_hangman_clue()

def math_game():

    game = Math(room, obj)
    game.show_game()
    game.show_math()

    while True:
        option = input("\nEscoja una opción: \n1. Responder pregunta.\n2. Pista\n--> ")
        while not option.isdigit() or int(option) not in range (1,3):
            option = input("\nEscoja una opción:\n1. Responder pregunta.\n2. Pista\n--> ")
        if option == "1":
            player_math_input = validate_player_math_input()
            answer = game.answer_math(player_math_input)
            if answer == True:
                break
        else:
            game.get_math_clue()
    
def validate_player_math_input():
    player_math_input = input("Ingrese su respuesta en fracciones: ")
    while True:
        try:
            float(player_math_input)
            break
        except ValueError:
            try:
                number, denom = player_math_input.split("/")
                float(number)
                float(denom)
                break
            except:
                print("\nIngreso inválido, por favor, ingrese un número.")
                player_math_input = input("Ingrese su respuesta en fracciones: ")
    return player_math_input

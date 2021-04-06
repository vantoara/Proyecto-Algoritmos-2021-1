from Player import Player
from Guessing import Guessing
from Word_Search import Word_Search
from Crypto import Crypto
from Hangman import Hangman
from Math import Math
from Python import Python
from Boolean import Boolean
from Number import Number
from Shuffle import Shuffle
from Quiz import Quiz
from Memory import Memory
from Logic import Logic
from Color import Color
from Room import Room
import requests
import random
import enquiries
import json

import requests

api = requests.get("https://api-escapamet.vercel.app")

# Función utilizada para el quiz número 1
def validate_password():
    print("\nSu contraseña debe tener más de 8 caracteres, tener al menos un número, una letra mayúscula, una letra minúscula y un caracter especial")
    while True:
        password = input("\nIngrese su nueva contraseña: ")
        if len(password) < 8:
            print("\nLa contraseña elegida no es válida.")
        else:
            #Los any iteran a través de los varios for loops y si UN solo caracter cumple la condición (regresa True) entonces, la condición regresará True, por  ende, utilicé varios any (varios for loop idénticos) para ver que las condiciones de la contraseña se cumplan.
            if any(character.isspace() for character in password):
                print("\nLa contraseña elegida no es válida. Ingresaste un espacio.")
            else:
                if (not any(character.isdigit() for character in password)) or (not any(character.isalpha() for character in password)):
                    print("\nLa contraseña elegida no es válida. Carece de números o letras.")
                else:
                    if any(character.islower() for character in password) and any(character.isupper() for character in password):
                        if any(not character.isalnum() for character in password):
                            print("\nContraseña ingresada correctamente")
                            break
                        else:
                            print("\nLa contraseña elegida no es válida. Debe añadir un caracter especial.")
                    else:
                        print("\nLa contraseña elegida no es válida. Necesita tanto letras mayúsculas como minúsculas.")
    return password

def registry(database):

    # Aquí se registrarán los usuarios por primera vez.

    user = input("\nIngrese su nombre de usuario: ")
    if user in database:
        print("\nIngreso inválido, usuario ya registrado.")
        return database
        # Aquí no hay ningún loop ya que si es un usuario que está registrado, puede ser que a la persona simplemente se le haya olvidado, por ende, esto lo enviaría de una vez al menú principal.
    while len(user) < 3 or len(user) > 8:
        print("\nNombre de usuario es muy largo o muy corto. Debe de ser entre 3 y 8 caracteres.")
        user = input("\nIngrese su nombre de usuario: ")
    password = validate_password() # Ya validado en la función anterior
    age = input("\nIngrese su edad: ")
    while not age.isdigit() or int(age) < 16:
        print("\nEdad es inválida. Recuerde que debe ser mayor de 16 años para poder jugar.")
        age = input("\nIngrese su edad: ")

    # Al registrar el usuario, como no está comenzando una partida, no me interesa en lo absoluto lo demás.
    player = Player(user.strip(), password, int(age))
    # Se me guarda como un diccionario siendo el user la llave, así cuando se inicie una nueva partida y pida el user, puedo jalar información fácilmente
    database[user] = player

    return database

def start_new_game(database):
    # Vuelvo a pedir user así corroboro si está creado
    user = (input("\nIngrese su nombre de usuario para poder jugar: ")).strip()
    while len(user) < 3 or len(user) > 8:
        print("\nNombre de usuario es muy largo o muy corto. Debe de ser entre 3 y 8 caracteres.")
        user = (input("\nIngrese su nombre de usuario para poder jugar: ")).strip()

    if user in database:
        # Si el usuario existe es porque hay un objeto asignado a ese usuario, lo jalo y lo guardo en la variable player para mayor simplicidad
        player = database[user]

        while True:
            password = input("\nIngrese su contraseña: ")
            if password == player.get_password():

                #La librería enquiries permite un menú de selección de opciones el cual no necesita validar y es bastante práctico, solo requiere pasar la lista con las opciones deseadas como parámetro.
                difficulty_options = ["Fácil", "Medio", "Difícil"]
                difficulty_choice = enquiries.choose("\nEscoja una dificultad: ", difficulty_options)

                if difficulty_choice == "Fácil":
                    print("\nBienvenido, nuevo ingreso.")
                    player.set_difficulty(5.0, 5)
                    # Se implementan las distintas especificaciones dependiendo de cada . Las vidas se pasan como float por razones obvias.
                elif difficulty_choice == "Medio":
                    print("\nVeterano de barra.")
                    player.set_difficulty(3.0, 3)
                else:
                    print("\n¿Haces doble titulación, no?")
                    player.set_difficulty(1.0, 2)
                
                avatars = ["Scharifker", "Eugenio Mendoza", "Pelusa", "Gandhi", "Metropavo", "Exodia", "Lorenzo Mendoza", "Becado"]
                choose_avatar = enquiries.choose("\nEscoje uno de los siguientes avatares: ", avatars)
                player.set_avatar(choose_avatar)

                print("\nHoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?\n")

                # Si te llegas a morir entonces el while loop se rompe (consecuentemente ocurre lo mismo en las funciones nested) y se para el 
                while player.check_lives():
                    won = movement(player, api) # Esta función se encuentra al final, ya que a continuación se desarrollan son los distintos juegos.
                    if won:
                        break
                
                # Este if agarra el caso en el que perdiste tus vidas y hace un break que te arrojará al inicio del menú
                if not player.check_lives():
                    print("\nMuy mala jugada, te has quedado sin vidas!")
                    break
                
                else:
                    print(f"\nFelicitaciones, este trimeste ha sido muy difícil para todos, y a pesar de las desdichas y las angustias has podido entregar el Disco Duro a su lugar correspondiente. La universidad se encuentra agradecida contigo, {player.avatar}.")
                    break

            else:
                print("\nContraseña incorrecta!")

    else:
        # Igualmente, para qué hacer un while loop si no se encuentra registrado. Es innecesario.
        print("\nEste usuario no se encuentra registrado.")

# Para toda función de juego le paso room, obj (objeto) y el objeto player; room y obj para la clase (que se detalla en Game.py) y player para poder modificar los atributos como es debido
# Adivinanzas
def guessing_game(room, obj, player):

    game = Guessing(room, obj)
    # Este if lo que valida es si el jugador ya completó el minijuego, es decir, si tienes la recompensa en tu inventario es porque jugaste este juego y lo completaste.
    if game.get_award() in player.get_inventory():
        print("\nYa completaste este juego. Anda, que el tiempo se agota.")

    else:
        # Valida si tengo los requisitos para jugar, se detalla más en Game.py
        if "contraseña" in player.get_inventory():

            print("Ingrese la contraseña...")
            print("\n"*5)
            print("Contraseña correcta!") # simulación de que se hizo un input de contraseña, aesthetic.

            game.show_game()
            game.show_question()

            while player.check_lives():
                options = ["Responder", "Pedir pista"]
                choice = enquiries.choose("\nEscoja que hacer: ", options)

                if choice == "Responder":
                    # No valido la respuesta a mayor profundidad ya que como el juego es una adivinanza, no lo amerita.
                    player_guess = input("\nIngrese su respuesta: ")
                    answer = game.guess(player_guess) # Retorna True o False y se valida si se resuelve o no la adivinanza
                    if answer == True:
                        print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                        player.add_item(game.get_award())
                        break
                    else:
                        player.update_lives(-0.5)
                        player.check_lives()

                else:
                    # Reviso si el jugador tiene pistas disponibles y si el juego tiene más pistas que dar. Si no se cumple, hay un mensaje de advertencia
                    if player.check_player_clues() and game.check_clue():
                        game.get_clue()
                        player.update_clues()
                        
# Sopa de Letras
def word_search_game(room, obj, player):

    game = Word_Search(room, obj)

    if "sopa_check" in player.get_inventory(): # El premio de la sopa de letras no es un objeto sino una vida extra, "sopa_check" es un string que se appendea a la lista de inventario y se tiene como un aval de que se completó el juego
        print("\n¿Memoria de corto plazo?. Ya completaste este juego.")

    else:

        if game.check_requirements(player.get_inventory()):
            game.show_game()
            # Método para mostrar la sopa. Se imprime una sola vez por tamaño y comodidad
            game.show_soup()

            while player.check_lives():
                options = ["Responder", "Pedir pista"]
                choice = enquiries.choose("\nEscoja que hacer: ", options)
                if choice == "Responder":
                    player_guess = ((input("Ingrese su respuesta: ")).lower()).strip()
                    while not player_guess.isalpha():
                        print("\nEntrada inválida, ingrese una palabra")
                        player_guess = ((input("Ingrese su respuesta: ")).lower()).strip()
                    # Podría colocar una validación para que el jugador evite ingresar números y demás, pero creo que es justo y necesario penalizarlos por su mala conducta y querer romper el programa.
                    # answer guarda si se completa el juego correctamente o no
                    answer = game.guess_word(player_guess, player)
                    if answer == True:
                        print("\nHas ganado una vida extra!")
                        player.update_lives(1.0) 
                        # El premio de la sopa de letras es una vida extra, así que se agrega al contador de vidas del jugador
                        player.add_item("sopa_check") # Append del aval
                        break

                else: 
                    if player.check_player_clues() and game.check_clue():
                        game.get_word_clue()
                        player.update_clues()

# Criptograma
def cryptic_game(room, obj, player):

    game = Crypto(room, obj)

    if "Mensaje" in player.get_inventory(): # Aquí busco "Mensaje" justamente ya que así es como está guardado de requisito para la API y otra habitación, así que para evitar mayores complicaciones, se verifica el dato directamente en lugar de hacer un get.award()
        print("\nPor aquí no es, ya resolviste este juego.")

    else:
        
        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_alphabet()
            game.show_encode()

            while player.check_lives():
                player_decode = (input("\nDescrife el código e ingrese su respuesta: ")).lower()
                # Podría colocar una validación para que el jugador evite ingresar números y demás, pero creo que es justo y necesario penalizarlos por su mala conducta y querer romper el programa.
                answer = game.answer_decode(player_decode)
                if answer == True:
                    change_award = game.get_award()
                    change_award = change_award.replace(": Si estas gradudado puedes pisar el Samán","")
                    print(f"\nHas ganado el siguiente objeto: {change_award}")
                    player.add_item(change_award)
                    break
                else:
                    player.update_lives(-1)
                # Criptograma no tiene pistas así que no nos interesa en lo absoluto.

# Ahorcado
def hangman_game(room, obj, player):
    
    game = Hangman(room, obj)
    
    if game.get_award() in player.get_inventory():
        print("\nQue por aquí ya pasaste, vete a otra parte!")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_prompt()

            while player.check_lives():
                options = ["Responder", "Pedir pista"]
                choice = enquiries.choose("\nEscoja que hacer: ", options)
                if choice == "Responder":

                    player_letter = (input("\nIngrese una letra: ")).lower()
                    while not player_letter.isalpha(): # Valido el input, ya que aquí si se trabaja NETAMENTE con letras
                        print("\nEntrada inválida. Por favor, ingrese una letra.")
                        player_letter = (input("\nIngrese una letra: ")).lower()
                    answer = game.guess_hangman(player_letter, player)
                    if answer == True:
                        print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                        player.add_item(game.get_award())
                        break
                    elif answer == False: # Debido a como la clase y su método correspondiente están programadas, hay que ser específicos aquí
                        break # Como la vida se va restando dentro de la clase, no hace falta colocar nada aquí además del break
                else:
                     if player.check_player_clues() and game.check_clue():
                        game.get_hangman_clue()
                        player.update_clues()

# Preguntas matemáticas
def math_game(room, obj, player):

    game = Math(room, obj)

    if "mate_check" in player.get_inventory():
        print("\nAfortunadamente sabes derivar, ya que completaste este juego.")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_math()

            while player.check_lives():

                options = ["Responder", "Pedir pista"]
                choice = enquiries.choose("\nEscoja que hacer: ", options)
                if choice == "Responder":

                    player_math_input = validate_player_math_input() # Esta función valida el input del usuario, ya que debe ser una fracción
                    answer = game.answer_math(player_math_input)
                    if answer == True:
                        print("\nHas ganado una vida extra!")
                        player.update_lives(1.0)
                        player.add_item("mate_check") # Se appendea el aval de que se completó el juego
                        break
                    else:
                        player.update_lives(-0.25)
                        break
                else:
                    if player.check_player_clues() and game.check_clue():
                        game.get_math_clue()
                        player.update_clues()
    
def validate_player_math_input(): # Valida el input del usuario para el juego de matemáticas
    player_math_input = (input("\nIngrese su respuesta en fracciones: ")).strip()
    while True:
        try:
            float(player_math_input)
            break
        except ValueError: # Si el except lo capta entonces es porque puede tener "/" es decir, ser una fracción
            try:
                number, denom = player_math_input.split("/")
                float(number)
                float(denom) # Se evalúan ambos por separado
                break
            except:
                print("\nIngreso inválido, por favor, ingrese un número.")
                player_math_input = input("\nIngrese su respuesta en fracciones: ")
    return player_math_input

# Preguntas python
def python_game(room, obj, player):

    game = Python(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nDemostraste que sabes lo básico de programación al completar este juego, no hay más nada que hacer aquí.")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_phrase()

            while player.check_lives():

                options = ["Responder", "Pedir pista"]
                choice = enquiries.choose("\nEscoja que hacer: ", options)

                if choice == "Responder":
                    player_python_answer = input("\nIngrese su código en una línea: ")
                    while "frase" not in player_python_answer:
                        print("\nPor favor, ingrese un código decente.") # Esto evalúa que AL MENOS ingresen la variable que guarda el string
                        player_python_answer = input("\nIngrese su código en una línea: ")
                    answer = game.answer_python(player_python_answer)
                    if answer == True:
                        print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                        player.add_item(game.get_award())
                        break
                    else:
                        player.update_lives(-0.5)
                        break
                else:
                    if player.check_player_clues() and game.check_clue():
                        game.get_py_clue()
                        player.update_clues()

# Preguntas booleanas
def boolean_game(room, obj, player):

    game = Boolean(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nAquí no tienes nada que hacer, ya destruiste la puerta con el martillo.")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_boolean_question()

            # Únicas posibles respuestas
            options = ["True", "False"]
            choice = enquiries.choose("\nEscoja que hacer: ", options)
            answer = game.answer_boolean(choice)
            if answer == True:
                print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                player.add_item(game.get_award())
            else:
                player.update_lives(-0.5)

# Entre número
def number_game(room, obj, player):

    game = Number(room, obj)

    if "Titulo Universitario" in player.get_inventory():
        print("\nTienes tan buena suerte como aquel que pasa las tres físicas en el primer intento. Ya terminaste este juego.")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_number_question()

            while player.check_lives():

                player_number = input("\nAdivine un número entero en el rango dado: ")
                while not player_number.isdigit(): # Validación que sea un entero
                    print("\nPor favor, ingrese un número.")
                    player_number = input("\nAdivine un número entero en el rango dado: ")
                answer = game.answer_number(player_number)

                if answer == True:
                    change_award = game.get_award()
                    change_award = change_award.replace("título Universitario","Titulo Universitario") # Temas de la API...
                    print(f"\nHas ganado el siguiente objeto: {change_award}")
                    player.add_item(change_award)
                    break
                elif answer == False:
                    player.update_lives(-0.25)
                    # No hay break, el juego no se detiene sino hasta que gane o muere.

                if player.check_player_clues():
                    # Este prompt siempre aparecerá después de cada ingreso fallido, por si el usuario quiere una pista
                    options_clue = ["Si", "No"]
                    choice_clue = enquiries.choose("\n¿Desea obtener una pista?", options_clue)
                    if choice_clue == "Si":
                            game.get_number_clue(player_number)
                            player.update_clues()

# Palabras Mezcladas
def shuffle_game(room, obj, player):

    game = Shuffle(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nYa completaste este juego. Pudiste descifrar las palabras mezcladas, ahora asegúrate que no hayas mezclado tu elección de carrera.")

    else:

        if game.check_requirements(player.get_inventory()):

            game.show_game()
            game.show_information()
            game.show_shuffle()

            while player.check_lives():

                player_shuffle_guess = (input("\nIngrese una palabra a ordenar: ")).strip()
                while not player_shuffle_guess.isalpha():
                    print("\nIngreso inválido, por favor ingrese una palabra.")
                    player_shuffle_guess = (input("\nIngrese una palabra a ordenar: ")).strip()

                answer = game.guess_shuffle(player_shuffle_guess)

                if answer == True:
                    print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                    player.add_item(game.get_award())
                    break

                elif answer == False:
                    player.update_lives(-0.5)

# Quizizz
def quiz_game(room, obj, player):

    game = Quiz(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nTe esforzaste mucho respondiendo el Quizizz, ya completaste esta actividad. Lástima que solo vale 1%")

    else:

        if game.check_requirements(player.get_inventory()):
            game.show_game()
            game.show_specs()

            while player.check_lives():

                menu_options = ["Responder", "Pista"]
                choice = enquiries.choose("\nEscoja una respuesta", menu_options)

                if choice == "Responder":
                    options = game.get_options()
                    player_choice = enquiries.choose("\nEscoja una respuesta", options)
                    answer = game.answer_quiz(player_choice)

                    if answer == True:
                        print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                        player.add_item(game.get_award())
                        break
                    else:
                        player.update_lives(-0.5)
                        break

                else:
                    if player.check_player_clues() and game.check_clue():
                        game.get_quiz_clue()
                        player.update_clues()

# Memoria de emojis
def memory_game(room, obj, player):

    game = Memory(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nNi instalandóte una memoria de 16gb de RAM te acuerdas que ya pasaste por aquí. Este juego ya lo completaste.")

    else:
        if game.check_requirements(player.get_inventory()):

            game.show_grid()
            game.show_game()
            # Para este juego en específico, se realizaron todas las funciones como métodos dentro de la clase
            answer = game.guess_card(player)
            if answer == True:
                print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                player.add_item(game.get_award())

def logic_game(room, obj, player):

    game = Logic(room, obj)

    if game.get_award() in player.get_inventory():
        print("\nNo estés buscando problemas, ya pisaste el Samán y sobreviviste, ahora continúa.")
    else:
        # REVISAR POR SEPARADO REQUIREMENTS. FOR LOOP.
        if "Mensaje" in player.get_inventory() and "Titulo Universitario" in player.get_inventory():

            game.show_game()
            game.show_logic_question()

            player_logic = input("\nIngresa un número entero como respuesta: ")
            while not player_logic.isdigit():
                print("\nEntrada inválida.")
                player_logic = input("\nIngresa un número entero como respuesta: ")
            answer = game.answer_logic(int(player_logic))
            if answer == True:
                print(f"\nHas ganado el siguiente objeto: {game.get_award()}")
                player.add_item(game.get_award())
            else:
                player.update_lives(-1)
        else:
            game.show_msg()
            player.update_lives(-1) # Con esto logramos penalizar al jugador por pisar el samán

# Sudoku
def final_game(room, obj, player):

    game = Color(room, obj)

    if "carnet" not in player.get_inventory() and "Disco Duro" not in player.get_inventory():
        game.show_msg()

    else:

        game.show_game()
        game.color_question()

        while player.check_lives():
            
            answer = game.choose_color()

            if answer == True:
                print("\nGanaste el juego! Pudiste recuperar el Disco")
                won = True
                return won
            elif answer == False:
                player.update_lives(-1)

def movement(player, api):
    # Comienzas en la biblioteca
    room = 1
    position = Room(room)
    print(f"\nBienvenido {player.get_avatar()}, gracias por tu disposición a ayudarnos a resolver este inconveniente,  te encuentras actualmente ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más rápido que un trimestre en este reto.")
    position.show_room()

    while player.check_lives():

        can_break_door = api.json()[3]["objects"][0]["game"]["award"] in player.get_inventory()
        options = ["Ir a otra habitación", "Interactuar"]
        choice = enquiries.choose("\n¿Qué quieres hacer?: ", options)
        
        if choice == options[0]:
            # Teniendo el cuenta el mapa del doc, tomé en cuenta las habitaciones que se encuentran a la derecha e izquierda de cada uno y así el jugador sigue el flujo correcto
            directions = ["Izquierda", "Derecha"]
            choice_direction = enquiries.choose("\nEscoje a que dirección quieres moverte", directions)
            if room == 0:
                if choice_direction == directions[0]:
                    room = 4
                else:
                    room = 3
            elif room == 1:
                if choice_direction == directions[0]:
                    room = 3
                else:
                    room = 2
            elif room == 2:
                if choice_direction == directions[0]:
                    room = 1
                else:
                    print("\nNo te puedes mover a esa dirección, ya no hay más habitaciones a tu derecha!")
            elif room == 3:
                if choice_direction == directions[0]:
                    if can_break_door:
                        room = 0
                    else:
                        print("\nNo puedes pasar por ahí, está cerrado! Intenta abrir la puerta.")
                else:
                    room = 1
            else:
                if choice_direction == directions[0]:
                    print("\nNo te puedes mover a esa dirección, ya no hay más habitaciones a tu izquierda!")
                else:
                    room = 0

            position = Room(room)
            print("\n"*40)
            position.show_room()

        else:
            objects = position.get_list_objects()
            choice_object = enquiries.choose("\nEscoge con cuál objeto desea interactuar: ", objects)
            object_index = objects.index(choice_object)
            position.show_object(object_index)

            if room == 0:
                if object_index == 0:
                    word_search_game(room, object_index, player)
                elif object_index == 1:
                    python_game(room, object_index, player)
                else:
                    guessing_game(room, object_index, player)

            elif room == 1:
                if object_index == 0:
                    hangman_game(room, object_index, player)
                elif object_index == 1:
                    math_game(room, object_index, player)
                else:
                    cryptic_game(room, object_index, player)

            elif room == 2:
                if object_index == 0:
                    logic_game(room, object_index, player)
                elif object_index == 1:
                    quiz_game(room, object_index, player)
                else:
                    memory_game(room, object_index, player)

            elif room == 3:
                if object_index == 0:
                    boolean_game(room, object_index, player)

            elif room == 4:
                if object_index == 0:
                    won = final_game(room, object_index, player)
                    if won:
                        break
                elif object_index == 1:
                    shuffle_game(room, object_index, player)
                else:
                    number_game(room, object_index, player)
    return won
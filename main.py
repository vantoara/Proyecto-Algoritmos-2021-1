from funciones import *
import requests
import json

api = requests.get("https://api-escapamet.vercel.app")

def main():

    database = {}
    rooms_visited = []
    
    print("\nBienvenido al juego de escaperoom de la UNIMET!")

    # Intenté guardar el database en un archivo pero me lanzó un error ya que mi diccionario consiste en llaves con el nombre "user" y de items que consisten en el objeto Player. En serio lo intenté pero no hallé manera, disculpen la falta de base de datos en el proyecto.
    # with open("Players_Database.txt","a") as file:
    #        file.write(json.dumps(database))

    if database == {}:
        print("\n¿Primera vez? Regístrate, no seas tímido!")
        registry(database)

    while True:

        options = ["Registrar usuario","Iniciar partida", "Ver instrucciones", "Salir"]
        choice = enquiries.choose("\nEscoja una opción: ", options)
        if choice == options[0]:
            registry(database)

        elif choice == options[1]:
            start_new_game(database)

        elif choice == options[2]:
            print("\nEste juego es un escape room, es decir, se te presenta una serie de habitaciones en la que tendrás que completar distintos juegos para obtener recompensas y así conseguir tu objetivo final, recuperar y regresar el disco duro con los datos de Sirius.\nTendrás un límite de pistas por partida así como un límite de vidas, las reglas de cada juego especifican que penalización recibirás en tu contador de vida en caso de que fracases.\nDeberás estar atento a los requisitos que se te piden así como las recompensas que obtengas, ya que será vital para tu progreso.\nEn relación a los controles, en ocasiones se te pedirá un input mientras que en otras se te presentará un menu de selección; por otro lado, navegarás de cuarto a cuarto, de izquierda a derecha mediante un menu de opciones.\n¡Buena suerte!\n")

        else:
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
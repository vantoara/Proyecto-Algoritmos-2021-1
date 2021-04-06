from funciones import *
import requests
import json

api = requests.get("https://api-escapamet.vercel.app")

def main():
    database = {}
    rooms_visited = []
    options = ["Registrar usuario","Iniciar partida", "Ver instrucciones", "Salir"]
    
    print("\nBienvenido al juego de escaperoom de la UNIMET!")

    # Intenté guardar el database en un archivo pero me lanzó un error ya que mi diccionario consiste en llaves con el nombre "user" y de items que consisten en el objeto Player. En serio lo intenté pero no hallé manera, disculpen la falta de base de datos en el proyecto.
    # with open("Players_Database.txt","a") as file:
    #        file.write(json.dumps(database))

    if database == {}:
        print("\n¿Primera vez? Regístrate, no seas tímido!")
        registry(database)

    while True:
        choice = enquiries.choose("\nEscoja una opción: ", options)
        if choice == options[0]:
            registry(database)

        elif choice == options[1]:
            start_new_game(database)

        elif choice == options[2]:
            pass

        else:
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
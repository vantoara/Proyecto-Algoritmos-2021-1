from funciones import *
import requests

api = requests.get("https://api-escapamet.vercel.app")

def main():
    database = {}
    rooms_visited = []
    options = ["Registrar usuario","Iniciar partida", "Ver instrucciones", "Salir"]
    
    if database == {}:
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
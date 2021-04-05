import requests

api = requests.get("https://api-escapamet.vercel.app")

class Room:

    def __init__(self, room):
        self.room = api.json()[room]
        self.objects = api.json()[room]["objects"]

    def get_list_objects(self):
        name_list = []
        for obj in self.objects:
            name_list.append((obj["name"]).title())
        return name_list #Este método se utiliza para construir el menú de opciones en cada cuarto y que objetos están disponibles para interactúar.
    
    def show_room(self): # Gráficas del juego
        print(self.room["name"])
        # if self.room == "utilizar indices del diccionario y jalar de gráficas o igualar a distintos nombres y jalar de gráficas"

    def show_object(self, obj_index): 
        print((self.room["objects"][obj_index]["name"]).title())

        
import requests
import random

api = requests.get("https://api-escapamet.vercel.app")

class Game:

    def __init__(self, room, obj):
        # Jala de la API todos los detalles dados de un juego
        self.requirement = api.json()[room]["objects"][obj]["game"]["requirement"]
        if self.requirement != False:
            # Jala el mensaje si es que hay un requisito
            self.msg = api.json()[room]["objects"][obj]["game"]["message_requirement"]
        self.name = api.json()[room]["objects"][obj]["game"]["name"]
        self.award = api.json()[room]["objects"][obj]["game"]["award"]
        self.rules = api.json()[room]["objects"][obj]["game"]["rules"]
        # question_choice selecciona cuál pregunta manejarán las demás variables, la más importante de todas
        self.question_choice = random.choice(api.json()[room]["objects"][obj]["game"]["questions"])

    def show_msg(self): # Método que utilizo para dos juegos únicamente
        if self.requirement != False:
            print("\n")
            print(self.msg)

    def show_game(self):
        print(f"\nNombre: {self.name}\nReglas: {self.rules}")

    def get_award(self):
        return self.award

    # Este método sirve para chequear los requisitos de un juego y si se puede jugar o no
    def check_requirements(self, player_inventory):
        if self.requirement != False: # Hay un requisito, así que se evalúa dentro de este if
            if self.requirement not in player_inventory:
                print("\n")
                print(self.msg)
                return False
            else:
                print(f"\nHas utlizado {self.requirement}.")
                return True
        else: # Si no hay requerimiento, pasa para acá
            return True

    def get_requirement(self):
        if self.requirement != False:
            return self.requirement
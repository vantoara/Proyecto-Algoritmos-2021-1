import requests
import random

api = requests.get("https://api-escapamet.vercel.app")

class Game:
    def __init__(self, room, obj):
        self.requirement = api.json()[room]["objects"][obj]["game"]["requirement"]
        if self.requirement != False:
            self.msg = api.json()[room]["objects"][obj]["game"]["message_requirement"]
        self.name = api.json()[room]["objects"][obj]["game"]["name"]
        self.award = api.json()[room]["objects"][obj]["game"]["award"]
        self.rules = api.json()[room]["objects"][obj]["game"]["rules"]
        # question_choice selecciona cuál pregunta manejarán las demás variables
        self.question_choice = random.choice(api.json()[room]["objects"][obj]["game"]["questions"])

    def show_game(self):
        if self.requirement != False:
            print(f"{self.msg}\nRequerimiento: {self.requirement}")
        print(f"Nombre: {self.name}\nReglas: {self.rules}")       
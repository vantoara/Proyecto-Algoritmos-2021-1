from Game import Game
import random

class Guessing(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        # Se establecen los detalles de la pregunta (pregunta en específico, lista de respuestas, etc.)
        self.clues = [self.question_choice["clue_1"], self.question_choice["clue_2"], self.question_choice["clue_3"]]
        self.given_clues = []
        self.question = self.question_choice["question"]
        self.answer = self.question_choice["answers"]

    def show_question(self):
        print(self.question)

    def get_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("Ya no hay más pistas")
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)
            return self.given_clues

    def guess(self, player_guess):
        if player_guess in self.answer:
            print("Respuesta Correcta!")
            return True
        else:
            print("Respuesta Incorrecta!")
            return False

from Game import Game
import random

class Logic(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice
        if self.question == "🧡+🧡+🧡=45 \n 🍌+🍌+🧡=23 \n 🍌+⏰+⏰=10 \n ⏰+🍌+🍌x🧡=?": # Por cuestions de API copié las preguntas a la clase y dependiendo de que pregunta le toqué el jugador, se espera una respuesta distinta.
            self.answer = 67
        else:
            self.answer = 41

    def show_logic_question(self):
        print(self.question)

    def answer_logic(self, player_logic):
        if player_logic == self.answer:
            print("Felicitaciones, sabes matemática de primer año!")
            return True
        else:
            print("Respuesta incorrecta, ¿quedaste en lista 5?")
            return False
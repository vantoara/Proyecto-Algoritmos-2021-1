from Game import Game
import random

class Python(Game):
    
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.answer = self.question_choice["answer"]
        self.clues = [self.question_choice["clue_1"], self.question_choice["clue_2"], self.question_choice["clue_3"]]
        self.given_clues = []
        if self.answer == "Validar en python que de el siguiente resultado: 50.00 en formato entero":
            self.result = 50
            self.phrase = "tengo en mi cuenta 50,00 $"
        else:
            self.result = "sistemas de ingenieria metro la en estudio"
            self.phrase = "oidutse ne al ortem aireinegni ed sametsis"

    def show_phrase(self):
        print("\nUtiliza la siguiente frase: ")
        print(f"frase = {self.phrase}")
    def answer_python(self):
        

        else:


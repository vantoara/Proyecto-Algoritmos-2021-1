from Game import Game
import random

class Quiz(Game):
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.answer = self.question_choice["correct_answer"]
        self.options = [self.question_choice["correct_answer"], self.question_choice["answer_2"], self.question_choice["answer_3"], self.question_choice["answer_4"]]
        # Revuelve el orden de las opciones
        random.shuffle(self.options)
        self.clue = [self.question_choice["clue_1"]]
        self.given_clue = []

    def show_specs(self):
        print("\n")
        print(self.question)

    def get_options(self):
        return self.options

    def answer_quiz(self, player_choice):
        if player_choice == self.answer:
            print("\nFelicidades! Escogiste la respuesta correcta!")
            return True
        else:
            print("\nLamentablemente, esa no era la respuesta.")
            return False

    def get_quiz_clue(self):
        if not self.check_clue():
            pass
        else:
            (self.given_clue).append(self.clue)
            print(*self.clue)
        
    def check_clue(self):
        if len(self.given_clue) == len(self.clue):
            print("\nYa no hay más pistas que dar.")
            return False
        else:
            return True
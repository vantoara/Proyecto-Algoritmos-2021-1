from Game import Game
from sympy import *
from fractions import Fraction
import random

class Math(Game):
    
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.clue = [self.question_choice["clue_1"]]
        self.given_clues = []
        self.list_question = self.question.split()
        self.value = (self.list_question[7].replace("pi","3.14"))
        function = self.list_question[8:]
        self.function = "".join(function).replace("f(x)=","").replace("sen(x)","sin(x)")
    
    def show_math(self):
        print("\n")
        print(self.question)
        print("Usar pi = 3.14 y utilizar calculadora en radianes. Redondear resultado a UN (1) decimal y responder en su fracción correspondiente")

    def convert_to_float(self):
        try:
            float(self.value)
        except ValueError:
            number, denom = self.value.split("/")
            try:
                self.value = round(float(self.number)/float(self.denom),2)
                return self.value
            except:
                return None

    def question_answer(self):
        self.convert_to_float()
        x = Symbol("x")
        derivative = (diff(self.function, x))
        evaluate = round(derivative.evalf(subs={x:self.value}),1)
        self.answer = frac = Fraction(str(evaluate))

    def answer_math(self, player_math_input):
        self.question_answer()
        if player_math_input == str(self.answer):
            print("Respuesta correcta. Sabes derivar!")
            return True
        else:
            print("Uy, no sabes derivar.")
            return False

    def get_math_clue(self):
        if len(self.given_clues) == len(self.clue):
            print("Ya no hay más pistas")
        else:
            new_clue = random.choice(self.clue)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clue)
            self.given_clues.append(new_clue)
            print(new_clue)
            return self.given_clues
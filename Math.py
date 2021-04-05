from Game import Game
from sympy import * # sympy nos calculará la derivada y su valor en un punto dado
from fractions import Fraction
import random

class Math(Game):
    
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.clue = [self.question_choice["clue_1"]]
        self.given_clues = []
        self.list_question = self.question.split() # me guarda en una lista el string de pregunta
        self.value = (self.list_question[7].replace("pi","3.14")) # una vez obtenido eso me jalo el valor de la lista que siempre se encuentra en la posición 7, reemplazo pi por 3.14 para su manejo
        function = self.list_question[8:]
        self.function = "".join(function).replace("f(x)=","").replace("sen(x)","sin(x)") # Me jalo la función de la API y elimino el inicio así como también reemplazo sen(x) por su equivalente en inglés y evitar problemas con sympy
        self.answer = ""
    
    def show_math(self): # Especifica al usuario las condiciones
        print("\n")
        print(self.question)
        print("Usar pi = 3.14 y utilizar calculadora en radianes. Redondear resultado a UN (1) decimal y responder en su fracción correspondiente")

    def convert_to_float(self):
        # Super importante, esto es lo que evalúa que el value jalado de la API sea un valor con el que trabajar fácilmente, ya sea un entero, decimal o fracción
        try:
            float(self.value)
        except ValueError:
            number, denom = self.value.split("/")
            try:
                self.value = float(number)/float(denom)
            except:
                return None

    def question_answer(self):
        # aquí entra sympy, me evalua la respuesta de la pregunta al calcular la derivada de la función e ingresar el valor que especifica la misma pregunta
        self.convert_to_float()
        x = Symbol("x") # sympy estable a x como una incógnita
        derivative = (diff(self.function, x)) # cálculo de la derivada
        evaluate = round(derivative.evalf(subs={x:self.value}),1) # le pasamos a la derivada el value ya calculado, regresando un valor decimal REDONDEADO
        self.answer = Fraction(str(evaluate)) # esta es la respuesta definitiva y con la que se comparará el input del usuario, convierte el valor previo de un decimal a una fracción

    def answer_math(self, player_math_input):
        self.question_answer()
        if player_math_input == str(self.answer):
            print("Respuesta correcta. Sabes derivar!")
            return True
        else:
            print("Uy, no sabes derivar.")
            return False

    def get_math_clue(self):
        if not self.check_clue(): # Este juego solo tiene una pista por lo que no hace falta la función tan larga como antes
            pass
        else:
            self.given_clues.append(self.clue)
            print(*self.clue)

    def check_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("Ya no hay más pistas que dar.")
            return False
        else:
            return True
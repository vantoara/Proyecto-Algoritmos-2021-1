# Este es mi plan b para el juego ya que el sudoku no quiso funcionar.

from Game import Game
import enquiries
import random

class Color(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.name = "Adivine el color"
        self.question = self.question_choice["question"]
        self.question = "Debe adivinar el color en el que estoy pensando... Cada 3 intentos fallidos pierdes una vida"
        self.colors = ["Amarillo", "Azul", "Rojo", "Verde", "Morado", "Naranja", "Negro", "Gris", "Fucsia"]
        self.answer = random.choice(self.colors)
        self.attempts = 3
        self.guessed_colors = []
    
    def color_question(self):
        print(self.question) # Imprime la pregunta que es customizada

    def choose_color(self):
        options = self.colors
        player_input = enquiries.choose("\nEscoje uno de los colores a considerar: ", options)

        if player_input in self.guessed_colors:
            print("\nYa adivinaste ese color!") # Si el input ya esta en la lista de colores adivinados entonces arroja este mensaje
        else:
            if player_input == self.answer:
                print("\nMuy bien, has adivinado el color!")
                return True
            else:
                self.attempts -= 1 # Intentos, tras tres intentos, el jugador pierde una vida
                self.guessed_colors.append(player_input)
                print("\nRespuesta equivocada, tienes mal gusto.")
                if self.attempts == 0:
                    return False
        
    
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

    # Aquí te devuelven un pista random si es que hay pistas que dar
    def get_clue(self):
        if not self.check_clue():
            pass
        else:
            new_clue = self.clues[0] 
            # A diferencia de los otros get_clue que arrojan pistas randomizadas, aquí en adivinanza las arroja en orden ya que tienen una jerarquía de importancia. Por ejemplo la última pista casi que te dice la palabra a adivinar, mientras que la primera es mucho más discreta.
            print(new_clue)
            self.clues.remove(new_clue)

    # Revisa si se han dado todas las pistas
    def check_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("\nYa no hay más pistas que dar.")
            return False
        else:
            return True
            
    # Este es el juego en sí, se le pasa un parámetro y se compara con la respuesta de la API ya instanciada
    def guess(self, player_guess):
        if player_guess in self.answer:
            print("\nRespuesta Correcta!")
            return True
        else:
            print("\nRespuesta Incorrecta!")
            return False

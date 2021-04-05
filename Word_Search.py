from Game import Game
import random
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel

class Word_Search(Game):
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.given_clues = []
        self.clues = [self.question_choice["clue_1"], self.question_choice["clue_2"], self.question_choice["clue_3"]]
        self.answer = [(self.question_choice["answer_1"]).lower(),(self.question_choice["answer_2"]).lower(),(self.question_choice["answer_3"]).lower()]
        self.guessed = []
        self.soup = create_panel(height = 15, width = 15, words_value_list = self.answer)

    def show_soup(self):
        # Gracias a la librería word_search_puzzle se puede implementar el método para mostrar un grid 15*15 randomizado de letras que incluyan las respuestas. Simplemente llamamos a la función y pásamos la lista con las palabras que queramos que aparezca
        print("\n")
        display_panel(self.soup.get("panel"))
    
    # Lista de palabras adivinadas
    def get_guessed(self):
        return self.guessed

    # Juego como tal, revisamos que el input no esté en las adivinadas, luego, si lo está se imprime la lista y se le advierte al jugador, si no lo está entonces se compara con la lista de respuestas.
    def guess_word(self, player_guess, player):
        if player_guess in self.guessed:
            print("\nYa descubriste esa palabra. Palabras descubiertas: ")
            print(self.get_guessed())
        else:
            self.show_soup()
            if player_guess in self.answer:
                print("\nRespuesta Correcta!")
                self.guessed.append(player_guess)
                # Este if solo se entra si ha adivinado todas las palabras
                if len(self.guessed) == len(self.answer):
                    print("\nHas resuelto la sopa de letras, felicidades!")
                    return True
            else:
                print("Respuesta Incorrecta!")
                player.update_lives(-0.5) # Se pasa el update_lives por aquí ya que esto depende de la palabra incorrecta
                
    def check_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("\nYa no hay más pistas que dar.")
            return False
        else:
            return True

    def get_word_clue(self):
        if not self.check_clue():
            pass
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)
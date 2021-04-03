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

    def show_soup(self):
        soup = create_panel(height = 15, width = 15, words_value_list = self.answer)
        display_panel(soup.get("panel"))
    
    def get_guessed(self):
        return self.guessed

    def guess_word(self, player_guess):
        if player_guess in self.guessed:
            print("Ya descubriste esa palabra:")
            print(self.get_guessed())
        else:
            if player_guess in self.answer:
                print("Respuesta Correcta!")
                self.guessed.append(player_guess)
                if len(self.guessed) == len(self.answer):
                    print("Ha resuelto la sopa de letras, felicidades!")
                    return True
            else:
                print("Respuesta Incorrecta!")

    def get_word_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("Ya no hay más pistas")
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)
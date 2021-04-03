from Game import Game
import random

class Hangman(Game):
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.prompt = self.question_choice["question"]
        self.hangman_answer = (self.question_choice["answer"]).lower()
        self.answer_set = set(self.hangman_answer)
        self.attempts = 6
        self.letters_guessed = set()
        self.clues = [self.question_choice["clue_1"], self.question_choice["clue_2"], self.question_choice["clue_3"]]
        self.given_clues = []

    def show_prompt(self):
        print(self.prompt)
        self.show_man()
        self.show_display()

    def show_display(self):
        display = ""
        for letter in self.hangman_answer:
            if letter in self.letters_guessed:
                display += letter
            else:
                display += "_"
        print(display)

    def show_man(self):
        print(the_hanged_man[self.attempts])
    
    def get_answer_set(self):
        return len(self.answer_set)

    def guess_hangman(self, player_letter):
        if player_letter in self.letters_guessed:
            print("Ya adivinaste esa letra.")
        else:
            if player_letter in self.answer_set:
                print("Letra correcta!")
                self.answer_set.remove(player_letter)
                if len(self.answer_set) == 0:
                    self.letters_guessed.add(player_letter) 
                    self.show_display()
                    print("\nAdivinaste la palabra!")
                    return True     
            else:
                print("Letra incorrecta!")
                self.attempts -= 1
                if self.attempts == 0:
                    print("Perdiste el juego. Quedaste ahorcado.")
                    return False
            self.letters_guessed.add(player_letter) 
        self.show_display()
        self.show_man()

    def get_hangman_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("Ya no hay más pistas")
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)
            return self.given_clues

the_hanged_man = {

        0:"""
                ___________
               |          | 
               |         ( )
               |         \\|/
               |         / \\
               |
        """,
        
        1: """
                ___________
               |          | 
               |         ( )
               |          |/
               |         / \\
               |
        """,
        2: """
                ___________
               |          | 
               |         ( )
               |          |
               |         / \\
               |
           """,
        3: """
                ___________
               |          | 
               |         ( )
               |          |
               |         / 
               |
            """,
        4: """
                ___________
               |          | 
               |         ( )
               |          |
               |          
               |
            """,
        5: """
                ___________
               |          | 
               |         ( )
               |          
               |          
               |
            """,
        6: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
    }
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
        self.show_display() # Este método es el inicio en el que te muestra lo relevante a saber

    def show_display(self):
        display = ""
        for letter in self.hangman_answer:
            if letter in self.letters_guessed:
                display += letter
            else:
                display += "_"
        print("\n")
        print(display) # Esto imprime la palabra a medida que vas descubriendo las letras correspondientes

    def show_man(self):
        print(the_hanged_man[self.attempts]) # Imprime al muñequito
    
    def get_answer_set(self):
        return len(self.answer_set)

    # Juego como tal, se le pasa el parámetro player_letter que es la letra a adivinar y player es el objeto para modificarle la vida directamente, ya que esta se reduce por letra incorrecta
    def guess_hangman(self, player_letter, player):
        if player_letter in self.letters_guessed:
            print("\nYa adivinaste esa letra.")
        else:
            if player_letter in self.answer_set:
                print("\nLetra correcta!")
                self.answer_set.remove(player_letter) # Esto va aclarando el set de las letras que tiene las respuesta (set por razones obvias). Si es 0 entonces es que las adivinaste todas y allí entra en el siguiente if
                if len(self.answer_set) == 0: 
                    self.letters_guessed.add(player_letter) 
                    self.show_display()
                    print("\nAdivinaste la palabra!")
                    return True     
            else:
                print("\nLetra incorrecta!")
                self.attempts -= 1
                player.update_lives(-0.25)
                if self.attempts == 0:
                    print("\nPerdiste el juego. Quedaste ahorcado.")
                    return False # Perdiste el juego porque se te acabaron los 6 intentos
            self.letters_guessed.add(player_letter) 
        self.show_man()
        self.show_display()

    # Revisa si se han dado todas las pistas
    def check_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("\nYa no hay más pistas que dar.")
            return False
        else:
            return True
    
    def get_hangman_clue(self):
        if not self.check_clue():
            pass
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)

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
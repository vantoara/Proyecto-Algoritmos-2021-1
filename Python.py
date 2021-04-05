from Game import Game
import random

class Python(Game):
    
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.answer = self.question_choice["answer"]
        self.given_clues = []
        # Ok en este juego se tabulan los valores debido a lo específico que son entonces, se escoje una al azar y la respuesta, así como los atributos que esto conlleva, se seleccionan cuidadosamente dependiendo de que pregunta haya tocado.
        if self.answer == "Validar en python que de el siguiente resultado: 50.00 en formato entero":
            # Los self.phrase sirven como el parámetro a utilizar en el eval()
            self.result = 50
            self.phrase = "tengo en mi cuenta 50,00 $"
            self.clues = [self.question_choice["clue_1"], self.question_choice["clue_2"], self.question_choice["clue_3"]]
        else:
            self.result = "sistemas de ingenieria metro la en estudio"
            self.phrase = "oidutse ne al ortem aireinegni ed sametsis"
            self.clues = [self.question_choice["clue_1"]]

    def show_phrase(self):
        print(self.question)
        print("\nUtiliza la siguiente frase: ")
        print(f"frase = {self.phrase}") # Se le especifica al usuario que esta es la variable donde se guarda el string que tiene que modificar

    # Función que ejecuta el juego en si
    def answer_python(self, player_python_answer):
        frase = self.phrase
        try:
            eval(player_python_answer) # Estre try ve si el código corre o si lanza algún error
        except:
            print("\nNi siquiera corre.") # En caso de que el input arroje un error, retorna false porque no se vuelve a evaluar y así evitamos errores
            return False
        if eval(player_python_answer) == self.result:
            print("\n¡Correcto!")
            return True    
        else: # Este es el caso para un código que si se ejecute correctamente pero que lo que retorne no coincida con la respuesta tabulada
            print("\nCódigo incorrecto!")
            return False

    def get_py_clue(self):
        if not self.check_clue():
            pass
        else:
            new_clue = random.choice(self.clues)
            while new_clue in self.given_clues:
                new_clue = random.choice(self.clues)
            self.given_clues.append(new_clue)
            print(new_clue)

    def check_clue(self):
        if len(self.given_clues) == len(self.clues):
            print("\nYa no hay más pistas que dar.")
            return False
        else:
            return True
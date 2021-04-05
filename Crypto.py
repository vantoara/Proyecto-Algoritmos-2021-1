from Game import Game
import string
from caesarcipher import CaesarCipher # Librería para codificar
from terminaltables import AsciiTable

class Crypto(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.sentence = (self.question_choice["question"]).lower()
        self.move_letter = self.question_choice["desplazamiento"]

    # Con esto lo que logro es sustituir letras que no están en ASCII por letras que si
    def normalize(self):
        accents = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "ñ":"n"}
        sentence = list(self.sentence)
        for index, character in enumerate(sentence):
            for key, item in accents.items():
                if character == key:
                    sentence[index] = item
        self.sentence = "".join(sentence)
        return self.sentence   

    def show_alphabet(self): # Muestra el abecedario original sobre el abecedario encriptado.
        alphabet = string.ascii_lowercase
        alphabet_moved = CaesarCipher(alphabet, offset= self.move_letter)
        table_alphabet = [alphabet, alphabet_moved.encoded]
        table = AsciiTable(table_alphabet)
        print("\nGuía:")
        print(table.table)

    def show_encode(self):
        self.normalize() # Como dice, "normalizo" la oración dada
        # La librería es quien se encarga de encriptar el mensaje, self.move_letter corresponde con el desplazamiento, por lo que si cambia, se adapta el código   
        cryptic_msg = CaesarCipher(self.sentence, offset= self.move_letter)
        print(f"\nEl mensaje a descifrar es:\n{cryptic_msg.encoded}")

    def answer_decode(self, player_decode): # Función que resuelve el juego como tal, bastante straightforward
        if player_decode == self.sentence.lower():
            print("\nHa descifrado la oración correctamente!")
            return True
        else:
            print("\nNo ha descrifrado correctamente la oración.")
            return False
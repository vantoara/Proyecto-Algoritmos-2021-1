from Game import Game
import random

class Shuffle(Game):
    
    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.category = self.question_choice["category"]
        self.word_list = self.question_choice["words"]
        self.word_list = [word.lower() for word in self.word_list] 
        self.guess_word_list = [word.lower() for word in self.word_list]
        #Tenemos dos listas iguales, word_list que es la original ya arreglada y guessed_word_list que es la organizada y se irá modificando a lo largo del juego.
        self.shuffle_list = []
        self.shuffle_words()

    def shuffle_words(self):
        for word in self.word_list:
            word_shuffle = random.sample(word, len(word))
            # Sample lo que hace es revolver la palabra y separarla y luego con el join se junta la palabra nueva formada (revuelta)
            word_shuffle = "".join(word_shuffle)
            self.shuffle_list.append(word_shuffle)
            # De aquí obtenemos las palabras mezcladas al azar
    
    def show_information(self):
        print(self.question)
        print("\nTen en mente que la lista pertenece a la siguiente categoría: ")
        print(self.category)
        # Método que especifica la categoría, un atributo particular de este juego

    def show_shuffle(self):
        print("\nLista de palabras: ")
        for word in self.shuffle_list:
            print(word)
        # Muestra la lista mezclada
    
    def guess_shuffle(self, player_shuffle_guess):
        # Verificamos que el input esté en la lista original que siempre permanece igual, es nuestra primera referencia
        if player_shuffle_guess in self.word_list:
            # Verificamos que no esté en la lista de las palabras adivinadas. A esa lista se le ELIMINA las adivinadas.
            if player_shuffle_guess not in self.guess_word_list:
                print("\nYa adivinaste esa palabra")
            else:
                # Aquí primero se trae el índice de la palabra en la lista original, y ese mismo índice (ya que todos coinciden) se iguala al elemento en ese índice en la list mezclada al input, para así mostrar las palabras ya ordenadas junto a las que le faltan.
                self.shuffle_list[self.word_list.index(player_shuffle_guess)] = player_shuffle_guess
                # Aquí también se le elimina a la adivinada para comparar más fácilmente
                self.guess_word_list.remove(player_shuffle_guess)
                print("\nDescubriste una palabra, felicitaciones!")
                # Se cumple la condición de que descubriste todas, por ende, ganaste.
                if len(self.guess_word_list) == 0:
                    print("\nDescubriste todas las palabras, felicidades!")
                    return True     
        else:
            print("\nEsa palabra no está en la lista!")
            return False
        # Aquí sin importar lo que pase, se imprime la lista actualizada de las palabras mezcladas
        self.show_shuffle()      
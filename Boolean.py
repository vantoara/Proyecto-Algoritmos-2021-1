from Game import Game

class Boolean(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        self.answer = (self.question_choice["answer"]).title()

    def show_boolean_question(self):
        print(self.question)

    def answer_boolean(self, player_boolean):
        #No hay pistas y solo se hace una simple comprobación, bastante straightforward
        if player_boolean == self.answer:
            print("Respuesta correcta!")
            return True
        else:
            print("Respuesta incorrecta.")
            return False
from Game import Game
import random

class Number(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.question = self.question_choice["question"]
        list_question = (self.question.replace("-"," ")).split()
        # Se hace un split de la oración dada y se reemplaza el guíon, así, los últimos dos items en la lista generada van a ser los intervarlos deseados. Se realizó de esta manera para aguantar cambios en la API.
        self.minimum = int(list_question[-2])
        self.maximum = int(list_question[-1])
        # cuando se inicia el juego ya se escoje un número aleatorio en el intervalo
        self.answer = random.randint(self.minimum, self.maximum)
        self.count_fail = 0

    def show_number_question(self):
        print(self.question)

    def answer_number(self, player_number):
        # Esta primera validación verifica que si el usuario ingresa un número fuera del intervalo, es incorrecto. Y pierde vida por dársela de creativo.
        if int(player_number) < self.minimum or int(player_number) > self.maximum:
            print("\nFuera de ranking! Pierdes igual.")
            self.count_fail += 1

        # A partir de aquí se valida como siempre.
        elif int(player_number) == self.answer:
            print("\nCorrecto! Lo adivinaste!")
            return True
        else:
            print("\nMala suerte! No lo lograste!")
            self.count_fail += 1
        # El count_fail lo que hace es ver que cuando se cumplan tres ingresos fallidos/incorrectos consecutivos (si se contesta correctamente ya el programa regresa True) y regrese False además de reiniciar su valor a 0.
        if self.count_fail == 3:
            self.count_fail = 0
            return False

    def get_number_clue(self, player_number):
        # Estos intervalos determinan la proximidad del ÚLTIMO número ingresado por el jugador, con el fin de darle una idea de qué tan cerca está.
        if (self.answer - 1) == int(player_number) or int(player_number) == (self.answer + 1):
            print("\nEstás muy muy cerca.")
        elif (self.answer) < int(player_number) <= (self.answer + 3):
            print("\nEstás cerca por arriba. Baja un poco más.")
        elif (self.answer - 3) <= int(player_number) < (self.answer):
            print("\nEstás cerca por abajo. Sube un poco más.")
        else:
            print("\nEstás perdido.")
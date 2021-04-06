# La idea original era un sudoku como juego final, sin embargo, no pude solventar algunos problemas al pedir el input de la columna, mi idea era hacer un código similar al que tenía en el juego de Memoria.

# No lo incluí en el diagrama de clases porque NO lo utilizo, está sin validar, lo dejé para terminarlo a futuro así como también reflejar mi esfuerzo.

from Game import Game
from sudoku import Sudoku
import enquiries

class Sudoku_Game(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.name = "Sudoku"
        self.question = self.question_choice["question"]
        self.question = "Tienes que jugar sudoku."
        self.board = [
            [0,0,7,0,4,0,0,0,1],
            [0,0,0,0,1,8,0,0,6],
            [0,4,1,0,0,0,9,0,0],
            [0,0,0,0,0,0,1,7,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,8,7,0,1,2,0,0],
            [3,1,0,0,0,0,0,0,0],
            [0,0,0,1,2,0,0,0,0],
            [8,6,0,0,7,0,0,1,5]
            ]

        self.board_solved = [
                [9,8,7,6,4,2,5,3,1],
                [2,3,5,9,1,8,7,4,6],
                [6,4,1,5,3,7,9,8,2],
                [5,2,6,3,8,4,1,7,9],
                [1,7,3,2,9,6,8,5,4],
                [4,9,8,7,5,1,2,6,3],
                [3,1,9,8,6,5,4,2,7],
                [7,5,4,1,2,3,6,9,8],
                [8,6,2,4,7,9,3,1,5]
        ]
        # question_choice selecciona cuál pregunta manejarán las demás variables, la más importante de todas

    def show_grid(self):
        self.grid = Sudoku(3, 3, board=self.board)
        self.grid.show()

    def show_sudoku_question(self):
        print(self.question)

    def coordinates(self):
    # Método el cual sirve como el input de las coordenadas en el juego
        options = [x for x in range(1,10)]
        coordinate_x = enquiries.choose("\nEscoje una fila: ", options)
        coordinate_y = enquiries.choose("\nEscoje una columna: ", options)
        return coordinate_x, coordinate_y

    def show_sudoku(self):
        self.show_grid()

    def guess_sudoku(self, player):
        
        print(self.board)
        completed = False

        while player.check_lives() and not completed:

            x, y = self.coordinates()
            # Se trabaja con x-1 y y-1 en lugar de x y y debido al tema de los índices
            if self.board[x-1][y-1] != 0:
                print("\nYa está ocupada esa casilla.")
            
            else:
                numbers = [i for i in range(1,10)] # Opciones disponibles para columnas Y seleccion de números
                number_input = enquiries.choose("\nEscoje el número que crees que va allí: ", numbers)

                self.board[x-1][y-1] = number_input

                if self.board[x-1][y-1] == self.board_solved[x-1][y-1]:
                    if not any(0 in lists for lists in self.board):
                        print("Ganaste!")
                        completed = True
                        return True

                    self.show_sudoku()
                    print("\nAdivinaste correctamente!")
                    
                else:

                    self.grid[x-1][y-1] = 0
                    print("\nNo procede! Número incorrecto.")
                    player.update_live(-0.25)
                    self.show_sudoku()
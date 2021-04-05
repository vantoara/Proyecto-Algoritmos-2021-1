from Game import Game
from sudoku import Sudoku
import enquiries

class Sudoku_Game(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.name = "Sudoku"
        self.question = self.question_choice["question"]
        self.question = "Tienes que jugar sudoku."
        self.grid = Sudoku(3).difficulty(0.5)
        self.solved_grid = self.grid.solve()
        # question_choice selecciona cuál pregunta manejarán las demás variables, la más importante de todas

    def show_sudoku_question(self):
        print(self.question)

    def coordinates(self):
    # Método el cual sirve como el input de las coordenadas en el juego
        options = [x for x in range(1,10)]
        coordinate_x = enquiries.choose("\nEscoje una fila: ", options)
        coordinate_y = enquiries.choose("\nEscoje una columna: ", options)
        return coordinate_x, coordinate_y

    def show_sudoku(self):
        self.grid.show()
        self.solved_grid.show() #ELIMINAR DESPUÉS DE VALIDAR

    def guess_sudoku(self, player):

        while player.check_lives():
            numbers = [x for x in range(1,10)]
            x, y = self.coordinates()
            # Se trabaja con x-1 y y-1 en lugar de x y y debido al tema de los índices
            if self.grid[x-1][y-1] == 0:
                
                number_input = enquiries.choose("\nEscoje el número que crees que va allí: ", numbers)
                self.grid[x-1][y-1] = number_input

                if self.grid[x-1][y-1] == self.solved_grid[x-1][y-1]:

                    print("\nAdivinaste correctamente!")
                    if not any(0 in lists for lists in self.grid):
                        print("Ganaste!")
                        return True
                    
                else:
                    self.grid[x-1][y-1] = 0
                    print("\nNo procede! Número incorrecto.")
                    player.update_live(-0.25)
                
                self.show_sudoku()
                
            else:
                print("\nYa hiciste match en esa casilla!")




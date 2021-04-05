from Game import Game
import random
from tabulate import tabulate
import enquiries

class Memory(Game):

    def __init__(self, room, obj):
        super().__init__(room, obj)
        self.grid = [['😀', '🙄', '🤮', '🥰'], ['🤮', '😨', '🤓', '😷'], ['😨', '🤓', '🥰', '😷'], ['🤑', '🤑', '🙄', '😀']]
        # Por problemas con la API, copié la lista de emojis aquí directamente
        self.shuffle_grid = []
        self.shuffle()
        self.guess_grid = []
        self.guess()
    
    def get_length(self):
        return len(self.grid)
    
    def shuffle(self):
        temp_grid = random.sample(self.grid, len(self.grid)) # Esta variable temporal guarda una matriz con las filas cambiadas
        for lists in temp_grid:
            # Aquí es que se cambian los emojis dentro de una fila
            shuffled_row = random.sample(lists, len(lists))
            self.shuffle_grid.append(shuffled_row)

    def guess(self):
        # Este método sirve para imprimir el guess_grid con incógnitas al inicio del juego
        for lists in self.shuffle_grid:
            self.guess_grid.append([])
            for emoji in lists:
                emoji = "?"
                self.guess_grid[-1].append(emoji)

    def coordinates(self):
        # Método el cual sirve como el input de las coordenadas en el juego
        length_options = self.get_length()
        options = [x for x in range(1,length_options+1)]
        coordinate_x = enquiries.choose("\nEscoje una fila: ", options)
        coordinate_y = enquiries.choose("\nEscoje una columna: ", options)
        return coordinate_x, coordinate_y

    def want_clue(self, player):
        # Método para pedir una pista
        if player.check_player_clues(): # Chequea si hay pistas disponibles
            clue_options = ["Si", "No"]
            clue_choice = enquiries.choose("\n¿Desea obtener una pista?", clue_options)
            return clue_choice
        else:
            clue_choice = "No" # Lo igualo a No para mejor legibilidad de que ocurre
            print("\nIngrese las otras coordenadas manualmente:") # A partir de ahora cuando vaya a seleccionar el segundo par de coordenadas aparecerá este print
            return clue_choice

    def guess_card(self, player):

        while player.check_lives():

            x, y = self.coordinates()
            # Se trabaja con x-1 y y-1 en lugar de x y y debido al tema de los índices
            if self.guess_grid[x-1][y-1] == "?": # Si la casilla escogida es un "?" entonces se procede a realizar todo el proceso, de lo contrario, se lanza un mensaje de que ya está ocupado y vuelve a pedir coordenadas

                self.guess_grid[x-1][y-1] = self.shuffle_grid[x-1][y-1] # Esto lo que hace es destapar el emoji seleccionado

                self.show_grid() # Se muestra la matriz actual  

                clue_choice = self.want_clue(player) # Se pregunta si desea una pista, si la respuesta es que si, entra en el siguiente if

                if clue_choice == "Si":
                    for i in range(len(self.shuffle_grid)):
                        for j in range(len(self.shuffle_grid)):
                            if self.shuffle_grid[i][j] == self.guess_grid[x-1][y-1]: # en todas las posiciones de la matriz se busca a las coordenadas que coincidan con el emoji seleccionado (siempre serán dos)
                                self.guess_grid[i][j] = self.shuffle_grid[i][j] # Se iguala el valor, destapando todos
                                self.show_grid() # Se muestra la matriz actualizada
                                if not any("?" in lists for lists in self.guess_grid): # En el caso de utiliza la pista al final
                                    print("\n¡Ganaste!")
                                    return True
                    player.update_clues()
                    print("\nMatch!")
                
                else: # Si se escoge que no quieres una pista el programa continua por acá
                    x2, y2 = self.coordinates() # el segundo par de coordenadas para comparar
                    while x2 == x and y2 == y: # El caso en el que vuelvas a escoger la casilla ya seleccionada
                        print("\nEstás parado en esa casilla, escoge otra.")
                        x2, y2 = self.coordinates()
                    while self.guess_grid[x2-1][y2-1] != "?": # Si selccionas una casilla la destapada
                        print("\nEsa casilla ya está ocupada\nVuelve a escoger otra")
                        x2, y2 = self.coordinates()
                    self.guess_grid[x2-1][y2-1] = self.shuffle_grid[x2-1][y2-1] # Destapamos el segundo emoji
                    self.show_grid()
                    input("\nPresione enter para continuar.\n> ")
                    if self.shuffle_grid[x2-1][y2-1] == self.shuffle_grid[x-1][y-1]: # Aquí se utiliza el shuffle_grid que es la matriz"oculta" o mejor dicho, la respuesta, y se compara si los emojis son iguales en ambas coordenadas
                        self.guess_grid[x2-1][y2-1] = self.shuffle_grid[x2-1][y2-1] # Aquí se iguala la segunda coordenada en lamatrizguess_grid y se sustituye el ? con el emoji correspondiente desde shuffle_grid
                        self.show_grid()
                        print("\nMatch!")
                        if not any("?" in lists for lists in self.guess_grid): # El any chequea si NO HAY ni un solo "?", y si eso ocurre secumple que el jugador ganó
                            print("\n¡Ganaste!")
                            return True
                    else: # Si entras en este else es porque el emoji de la segunda coordenada era distinto
                        self.guess_grid[x-1][y-1] = "?" # Se vuelve a voltear el primer emoji seleccionado
                        self.guess_grid[x2-1][y2-1] = "?"
                        self.show_grid()
                        print("\nNo match.")
                        player.update_lives(-0.25)
            else:
                print("\nYa hiciste match en esa casilla!")


    def show_grid(self):
        # Con la librería tabulate se imprime la matriz con un formato más agradable
        print("\n"*40)
        print(tabulate(self.guess_grid, tablefmt="presto"))
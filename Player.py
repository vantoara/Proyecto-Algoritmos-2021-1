class Player:
    def __init__(self, user, pswd, age):
        self.user = user
        self.pswd = pswd
        self.age = age
        self.avatar = ""
        self.inventory = []
        self.lives = 0.0
        self.clues = 0

    def set_difficulty(self, lives, clues):
        self.lives = lives
        self.clues = clues

    def set_avatar(self, avatar):
        self.avatar = avatar

    def add_item(self,new_item):
        self.inventory.append(new_item)

    def get_inventory(self):
        return self.inventory

    def get_user(self):
        return self.user

    def get_password(self):
        return self.pswd

    def get_player_clues(self):
        return self.clues
    
    def update_lives(self, amnt): # Se le pasa la cantidad de vidas a las que se le quiere añadir o quitar
        if self.check_lives():
            self.lives += amnt
            print(f"\nTus vidas restantes son: {self.lives}.")

    def update_clues(self):
        if self.check_player_clues():
            self.clues -= 1 # Las pistas es un número entero y disminuyen de 1 a 1 así que con solo llamar el método, realiza todo
            print(f"\nTe quedan {self.clues} pistas restantes.")
        
    def check_lives(self): # Con esto se construyen while loops en base a la vida del jugador y si muere entonces se rompen
        if self.lives > 0:
            return True
        else:
            return False

    def check_player_clues(self): # Se utiliza para construir condicionales y así detener que el jugador pida/obtenga más pistas
        if self.clues != 0:
            return True
        else:
            print("\nYa no tienes más pistas durante el resto del juego!")
            return False

    def get_avatar(self):
        return self.avatar
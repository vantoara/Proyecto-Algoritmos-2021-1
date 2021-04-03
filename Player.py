class Player:
    def __init__(self, user, pswd, age):
        self.user = user
        self.pswd = pswd
        self.age = age
        self.avatar = ""
        self.inventory = []
        self.lives = 0
        self.clues = 0
        self.time = 0

    def set_game(self, avatar, lives, clues):
        self.avatar = avatar
        self.lives = lives
        self.clues = clues

    def add_item(self,new_item):
        self.inventory.append(new_item)
    
    def update_lives(self, amnt):
        self.lives += amnt
        print(f"Tus vidas restantes son: {self.lives}")
        return self.lives

    def get_avatar(self):
        return self.avatar
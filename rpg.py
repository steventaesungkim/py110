#Rewriting using objects

class Characters:
    def __init__(self, char_name, health, power):
        self.name = char_name
        self.health = health
        self.power = power
player1 = Characters("Hero")
player2 = Characters("Goblin")

    def status(self, health, power):
        self.health = health
        self.power = power

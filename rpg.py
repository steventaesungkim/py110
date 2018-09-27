# #Rewriting using objects


# player1 = Characters("Hero")
# player2 = Characters("Goblin")

# print(player1.name)
# print(player2.name)

# print(name.health)
# print(player1.namepower)
# print(player2.health)
# print(player2.power)


class Characters:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
    def alive(self, char_health):
        if char_health.health > 0:
            return True
        return False
   



class Hero(Characters):
    def __init__(self, health, power):
        self.name = "Hero"
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do %d damage to the Goblin. " % (self.power))
    def print_status(self):
        print("You have %d health and %d power. " % (self.health, self.power))
        


class Goblin(Characters):
    def __init__(self, health, power):
        self.name = "Enemy"
    def attack(self, hero):
        hero.health -= self.power
        print("You does %d damage to you. "% (self.power))
    def print_status(self):
        print("The Goblin has %d health and %d power. " % (self.health, self.power))





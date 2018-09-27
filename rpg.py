# #Hero vs Goblin


# player1 = Characters("Hero")
# player2 = Characters("Goblin")

# print(player1.name)
# print(player2.name)

# print(name.health)
# print(player1.namepower)
# print(player2.health)
# print(player2.power)


class Characters:
    def __init__ (self, name, health, power):
        self.health = health
        self.power = power
    def alive(self, health):
        if self.health > 0:
            return True
        return False


class Hero(Characters):
    def __init__ (self, health, power):
        self.name = "Hero"
    def attack(self, enemy):
        enemy.health -= self.power
        print("You did %d damage to the Goblin. " % (self.power))
    def print_status(self):
        print("You have %d health and %d power. " % (self.health, self.power))
        

class Goblin(Characters):
    def __init__ (self, health, power):
        self.name = "Enemy"
    def attack(self, hero):
        hero.health -= self.power
        print("The Goblin has done %d damage to you. "% (self.power))
    def print_status(self):
        print("The Goblin has %d health and %d power. " % (self.health, self.power))


class Zombie(Characters):
    def __init__ (self, health, power):
        self.name = "Walking Dead"
    def attack(self, Zombie):
        if enemy.health < self.health:
            hero.health -= self.power
        print("The Zombie is only attacking Hero")
    def print_status(self):
        return True
            


def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print("You have %d health and %d power." % (hero_health, hero_power))
        print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do %d damage to the goblin." % hero_power)
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does %d damage to you." % goblin_power)
            if hero_health <= 0:
                print("You are dead.")

main()





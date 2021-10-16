from attacks import Attacks


class Dinosaur:
    #Constructor
    def __init__(self, name):
        self.name = name
        
        self.health = 100
        self.attack_types = []
        self.energy = 100

    #Methods
    def attack(self, robot, index):
        robot.health -= self.attack_types[index].attack_power
        self.energy -= 10

    def add_attack(self):
        crunch = Attacks("Crunch", 100)
        rend = Attacks("Rend", 75)
        roar = Attacks("Roar", 30)
        self.attack_types.append(crunch)
        self.attack_types.append(rend)
        self.attack_types.append(roar)

    def get_attack(self, index):
        print("You selected " + self.attack_types[index].name)
        return self.attack_types[index]


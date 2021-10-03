from weapon import Weapon



class Robot:
    #Constructor
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = []
        self.energy = 100

    #Methods
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.energy -= 10
        
    def add_weapons(self):
       first_weapon = Weapon('Ragnarok',9999)
        second_weapon = Weapon("Plasma machete",5000)
        third_weapon = Weapon('grenade',8888)
        self.weapon.append(first_weapon)
        self.weapon.append(second_weapon)
        self.weapon.append(third_weapon)
    
    def get_a_weapon(self, index):
        print("You selected " + self.weapon[index].name)
        return self.weapon[int(index)]

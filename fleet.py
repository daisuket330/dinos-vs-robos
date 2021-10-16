class Weapon:
    def __init__(self,name,attack):
        self.name = name
        self.attack_pwr = attack

class Robot:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.weapon = []

    def add_weapon(self):
        first_weapon = Weapon('Ragnarok',9999)
        second_weapon = Weapon("Plasma machete",5000)
        third_weapon = Weapon('grenade',8888)
        self.weapon.append(first_weapon)
        self.weapon.append(second_weapon)
        self.weapon.append(third_weapon)


class Fleet:
    def __init__(self):
        self.robos = []
        self.add_robos()

    def add_robos(self):
        primary_robo = Robot('Alpha',8000)
        segundo_robo = Robot('Gamma',6666)
        tertiary_robo = Robot('Omega',9999)
        self.robos.append(primary_robo)
        self.robos.append(segundo_robo)
        self.robos.append(tertiary_robo)


def getHealth(self):
        return self.health  

def getAttack(self):
        return self.attack


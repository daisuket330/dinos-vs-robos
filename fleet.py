from robot import Robot

class Fleet:
    def __init__(self):
        self.robos = []
        self.add_robos()

    def add_robos(self):
        Alpha = Robot('Alpha')
        Gamma = Robot('Gamma')
        Omega = Robot('Omega')
        self.robos.append(Alpha)
        self.robos.append(Gamma)
        self.robos.append(Omega)
        Alpha.add_weapons()
        Gamma.add_weapons()
        Omega.add_weapons()


# def getHealth(self):
#         return self.health  

# def getAttack(self):
#         return self.attack


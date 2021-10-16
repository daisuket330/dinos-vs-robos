from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.add_robos()

    def add_robos(self):
        Alpha = Robot('Alpha')
        Gamma = Robot('Gamma')
        Omega = Robot('Omega')
        self.robots_list.append(Alpha)
        self.robots_list.append(Gamma)
        self.robots_list.append(Omega)
        Alpha.add_weapons()
        Gamma.add_weapons()
        Omega.add_weapons()


# def getHealth(self):
#         return self.health  

# def getAttack(self):
#         return self.attack


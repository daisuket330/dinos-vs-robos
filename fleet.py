from robot import 

class Fleet:
    def __init__(self):
        self.robos = []
        self.add_robos()

    def add_robos(self):
        Alpha = Robot('Alpha',8000)
        Gamma = Robot('Gamma',6666)
        Omega = Robot('Omega',9999)
        self.robos.append(primary_robo)
        self.robos.append(segundo_robo)
        self.robos.append(tertiary_robo)
        Alpha.add_weapons()
        Gamma.add_weapons()
        Omega.add_weapons()


# def getHealth(self):
#         return self.health  

# def getAttack(self):
#         return self.attack


class Dinosaur:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack_power = attack
        


class Herd:
    def __init__(self):
        self.dino = []     
            
    def add_dinos(self):
        dino_1 = Dinosaur('Rex',10000,15000)
        dino_2 = Dinosaur('Queen',8000,10000)
        dino_3 = Dinosaur('Tony',7000,9500)
        self.dino.append(dino_1)
        self.dino.append(dino_2)
        self.dino.append(dino_3)
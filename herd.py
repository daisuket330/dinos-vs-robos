from dino import Dinosaur
class Herd:
    def __init__(self):
        self.dino = [] 
        self.add_dinos()
            
    def add_dinos(self):
        dino_1 = Dinosaur('Rex')
        dino_2 = Dinosaur('Queen')
        dino_3 = Dinosaur('Tony')
        self.dino.append(dino_1)
        self.dino.append(dino_2)
        self.dino.append(dino_3)
        dino_1.add_attack()
        dino_2.add_attack()
        dino_3.add_attack()

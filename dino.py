class Dinosaur:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack_power = attack
        self.alive_status = True    

    def dino_stats(self,name,health,attackpwr):
        self.name = name
        self.health = health
        self.attack_power = attackpwr



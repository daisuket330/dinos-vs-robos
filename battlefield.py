from fleet import Robot
from dino import Dinosaur
from herd import Herd
from fleet import Fleet

class battlefield:
    def __init__(self): #Not a declaration but a constructor
        self.fleet = Fleet().create_fleet()
        self.herd = Herd()
        self.game = ""
        self.welcome = ""
        self.dino_turn= ""

    def run_game(self, run):
        self.game = run        

    def display_welcome(self):
        self.welcome = "Begin Game!"
        print (self.welcome)

    def battle(self):
         while (Fleet.health > 0  and  Herd.health > 0 ):
             for i in range(len(Fleet.robots)):
                 Robot.attack
                 
             for i in range(len(Herd.dinosaurs)):
                 Dinosaur.dino_attack

                  
    def dino_turn (self, dinosaur):
        
        self.Dinosaur_turn=  Dinosaur.dino_attack

        #something like robot health= robot health - Dino.attack_power
        
    def robo_turn(self, robot):

    dino health = Dinosaur.health - Robot.attack power

    def show_dino_opponent_options(self):
        self.


    def show_robo_opponents_options(self):

    
    def display_winners (self):



# 



    
# damage = combatant.getAttack()
 
# hp_loss =.getHealth() - damage)herd1 = Herd()
# combatant1 = herd1.dino[0]
# combatant2 = herd1.dino[1]
# combatant3 = herd1.dino[2]
# print(f'hello,{combatant1.name}.')
# print(f'hello,{combatant2.name}.')
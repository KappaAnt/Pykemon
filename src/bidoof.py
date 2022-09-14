import pygame
import random
from pygame import mixer
from src import Types
#import src.Types

class Bidoof(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        """
        Intializes model/sprite
        args, name x y and img_file
        returns none
        """        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #Bidoof's Stats
        self.health = 115
        self.attack_stat = 40
        self.defense_stat = 25
        #Bidoof's Attacks
        self.tackle = 50/100
        self.tackle_type = "normal"
        self.growl = 12.5/100
        self.growl_type = "normal"
        self.bite = 80/100
        self.bite_type = "dark"
        self.hype = 20/100
        self.hype_type = "normal"
        #Bidoof's Type
        self.main_type = "normal"
        self.second_type = ""
        #Opponent Stats
        self.player1Hp = 0
        self.player1Attack = 0
        self.player1Defense = 0
        
        self.move = 0
        
        #Text
        self.adaptiveString = ""
        self.name = "bidoof"
        
    def attack(self, player1_health, player1_defense_stat, player1_attack_stat, player1_target_type, player1_second_type):
        """
        Attacks player by random chance, has all math calculations
        args: player1_health player1_defense_stat player1_attack_stat player1_target_type player1_second_type 
        returns: none
        """
        rvalue = random.randrange(1,5)
        
        #This worked for charmander so should on bidoof too - Ant
        self.player1Hp = player1_health
        self.player1Attack = player1_attack_stat
        self.player1Defense = player1_defense_stat
        if self.health == 0:
            rvalue = 5
            
        if rvalue == 1:
            #Tackle            
            self.move = self.tackle * self.attack_stat
            
            hit_chance = random.randrange(1,11)
            if hit_chance == 10:
                print("Bidoof Missed Tackle!")
                self.adaptiveString = "Bidoof Missed Tackle!"
            else:
                if player1_second_type == "":
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.tackle_type)
                    if state == "null":
                        print("Bidoof Hit Tackle!")
                        print("Doesn't Effect Enemy...")
                    elif state == "less":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * .5)
                        print("Bidoof Hit Tackle!")
                        print("Is not very effective...")
                       
                    elif state == "more":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * 1.5)
                        print("Bidoof Hit Tackle!")
                        print("Attack super effective!!")
                        
                    elif state == "same":
                        print("Bidoof Hit Tackle!")
                        #crit_chance = random.randrange(1,11)
                        #if crit_chance == 10:
                        	#self.move = self.move*2
                        	#print("Bidoof landed a critical hit!")
                        self.player1Hp = player1_health - (self.move * (1 - (player1_defense_stat/100)))
                        
                else:
                    instance = Types.Types()
                    state = instance.typeLogic(player1_target_type, self.tackle_type) #Types.typeLogic(player1_target_type, self.tackle_type)
                    state2 = instance.typeLogic(player1_second_type, self.tackle_type)
                    modifier = 1
                    modifier2 = 1
                    if state == "null" or state2 == "null":
                        print("Bidoof Hit Tackle!")
                        print("Doesn't Effect Enemy...")
                        modifier = 0
                        modifier2 = 0
                    if state == "more":
                        modifier = 2
                    elif state == "less":
                        modifier = .5
                    if state2 == "more":
                        modifier2 = 2
                    elif state2 =="less":
                        modifier2 = .5
                    if modifier * modifier2 == 1:
                        print("Bidoof Hit Tackle!")
                    elif modifier * modifier2 == 1/4:
                        print("Bidoof Hit Tackle!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 1/2:
                        print("Bidoof Hit Tackle!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 2:
                        print("Bidoof Hit Tackle!")
                        print("Attack super effective!!")                        
                        print(modifier)
                    elif modifier * modifier2 == 4:
                        print("Bidoof Hit Tackle!")
                        print("Attack super effective!!!!")
                    self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * (modifier * modifier2))
                self.adaptiveString = "Bidoof Hit Tackle!"
                    
        elif rvalue == 2:
            #Growl
            self.move = self.growl
                                                   
            hit_chance = random.randrange(1,11)
            if hit_chance == 10:
                print("Bidoof Missed Growl!")
                self.adaptiveString = "Bidoof Missed Growl!"
            else:                                
                if player1_second_type == "":
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.tackle_type)
                    if state == "null":
                        print("Bidoof Hit Growl!")
                        print("Doesn't Effect Enemy...")
                    else:
                        print("Bidoof Hit Growl!")
                        self.player1Attack = player1_attack_stat * (1 - self.move) 
                else:
                    instance = Types.Types()
                    state = instance.typeLogic(player1_target_type, self.tackle_type) #Types.typeLogic(player1_target_type, self.tackle_type)
                    state2 = instance.typeLogic(player1_second_type, self.tackle_type)                   
                    if state == "null" or state2 == "null":
                        print("Bidoof Hit Growl!")
                        print("Doesn't Effect Enemy...")
                    else:
                        print("Bidoof Hit Growl!")
                        self.player1Attack = player1_attack_stat * (1 - self.move) 
            self.adaptiveString = "Bidoof Hit Growl!"           
                                               
        elif rvalue == 3:
            #Bite
            self.move = self.bite * self.attack_stat
                                                   
            hit_chance = random.randrange(1,4)
            if hit_chance == 3:
                print("Bidoof Missed Bite!")
                self.adaptiveString = "Bidoof Missed Bite!"
            else:
                
                if player1_second_type == "":
                    temp = Types.Types() 
                    state = temp.typeLogic(player1_target_type, self.bite_type)
                    if state == "null":
                        print("Bidoof Hit Bite!")
                        print("Doesn't Effect Enemy...")
                    elif state == "less":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * .5)
                        print("Bidoof Hit Bite!")
                        print("Is not very effective...")
                        
                    elif state == "more":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * 1.5)
                        print("Bidoof Hit Bite!")
                        print("Attack super effective!!")
                        
                    elif state == "same":
                        print("Bidoof Hit Bite!")
                        self.player1Hp = player1_health - (self.move * (1 - (player1_defense_stat/100)))
               
                else:
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.bite_type)
                    state2 = temp.typeLogic(player1_second_type, self.bite_type)
                    modifier = 1
                    modifier2 = 1
                    if state == "null" or state2 == "null":
                        print("Bidoof Hit Bite!")
                        print("Doesn't Effect Enemy...")
                        modifier = 0
                        modifier2 = 0
                    if state == "more":
                        modifier = 2
                    elif state == "less":
                        modifier = .5
                    if state == "more":
                        modifier2 = 2
                    elif state =="less":
                        modifier2 = .5
                    if modifier * modifier2 == 1:
                        print("Bidoof Hit Bite!")
                    elif modifier * modifier2 == 1/4:
                        print("Bidoof Hit Bite!")
                        print("Is not very effective......")
                    elif modifier * modifier2 == 1/2:
                        print("Bidoof Hit Bite!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 2:
                        print("Bidoof Hit Bite!")
                        print("Attack super effective!!") 
                    elif modifier * modifier2 == 4:
                        print("Bidoof Hit Bite!")
                        print("Attack super effective!!!!")                    
                    self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * (modifier * modifier2))
                self.adaptiveString = "Bidoof Hit Bite!" 
                                    
        elif rvalue == 4:
            #Hype
            self.move = self.hype
                                                   
            hit_chance = random.randrange(1,11)
            if hit_chance == 10:
                print("Bidoof Missed Hype!")
                self.adaptiveString = "Bidoof Missed Hype!"
            else:
                print("Bidoof Hit Hype!")
                self.adaptiveString = "Bidoof Used Hype!"
                self.attack_stat = self.attack_stat * (1 + self.move)
                
        if self.player1Hp < 1:
            self.player1Hp = 0                                       
        

    def remember(self, hp, defense, attack):
        """
        Lets enemy and partner keep track of stats
        args: hp defense attack 
        returns none
        """

        self.health = hp
        self.defense_stat = defense
        self.attack_stat = attack
        
    def reset(self):
        """
        Resets stats
        args none
        returns none
        """

        self.health = 120
        self.defense_stat = 25
        self.attack_stat = 40 
        

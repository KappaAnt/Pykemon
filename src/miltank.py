import pygame
import random
from pygame import mixer
from src import Types
#import src.Types

class Miltank(pygame.sprite.Sprite):
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
        #Miltank's Stats
        self.health = 145
        self.attack_stat = 45
        self.defense_stat = 45
        #Miltank's Attacks
        self.stomp = 65/100
        self.stomp_type = "normal"
        self.growl = 12.5/100
        self.growl_type = "normal"
        self.fling = 40/100
        self.fling_type = "dark"
        self.milk_drink = 20/100
        self.milk_drink = "normal"
        #Miltank's Type
        self.main_type = "normal"
        self.second_type = ""
        #Opponent Stats
        self.player1Hp = 0
        self.player1Attack = 0
        self.player1Defense = 0
        
        self.move = 0
        
        #Text
        self.adaptiveString = ""
        self.name = "miltank"
        
    def attack(self, player1_health, player1_defense_stat, player1_attack_stat, player1_target_type, player1_second_type):
        """
        Attacks player by random chance, has all math calculated
        args: player1_health player1_defense_stat player1_attack_stat player1_target_type player1_second_type
        returns: none
        """
        rvalue = random.randrange(1,5)
        
        #This worked for charmander/breloom so should on bidoof/miltank too - Ant
        self.player1Hp = player1_health
        self.player1Attack = player1_attack_stat
        self.player1Defense = player1_defense_stat
        
        if self.health == 0:
            rvalue = 5
            
        if rvalue == 1:
            #Stomp            
            self.move = self.stomp * self.attack_stat
            
            hit_chance = random.randrange(1,11)
            if hit_chance == 10:
                print("Miltank Missed Stomp!")
                self.adaptiveString = "Miltank Missed Stomp!"
            else:
                if player1_second_type == "":
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.stomp_type)
                    if state == "null":
                        print("Miltank Hit Stomp!")
                        print("Doesn't Affect Enemy...")
                    elif state == "less":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * .5)
                        print("Miltank Hit Stomp!")
                        print("Is not very effective...")
                       
                    elif state == "more":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * 1.5)
                        print("Miltank Hit Stomp!")
                        print("Attack super effective!!")
                        
                    elif state == "same":
                        print("Miltank Hit Stomp!")
                        #crit_chance = random.randrange(1,11)
                        #if crit_chance == 10:
                        	#self.move = self.move*2
                        	#print("Bidoof landed a critical hit!")
                        self.player1Hp = player1_health - (self.move * (1 - (player1_defense_stat/100)))
                        
                else:
                    instance = Types.Types()
                    state = instance.typeLogic(player1_target_type, self.stomp_type) #Types.typeLogic(player1_target_type, self.tackle_type)
                    state2 = instance.typeLogic(player1_second_type, self.stomp_type)
                    modifier = 1
                    modifier2 = 1
                    if state == "null" or state2 == "null":
                        print("Miltank Hit Stomp!")
                        print("Doesn't Affect Enemy...")
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
                        print("Miltank Hit Stomp!")
                    elif modifier * modifier2 == 1/4:
                        print("Miltank Hit Stomp!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 1/2:
                        print("Miltank Hit Stomp!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 2:
                        print("Miltank Hit Stomp!")
                        print("Attack super effective!!")                        
                        print(modifier)
                    elif modifier * modifier2 == 4:
                        print("Miltank Hit Stomp!")
                        print("Attack super effective!!!!")
                    self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * (modifier * modifier2))
                self.adaptiveString = "Miltank Hit Stomp!"
                    
        elif rvalue == 2:
            #Growl
            self.move = self.growl
                                                   
            hit_chance = random.randrange(1,11)
            if hit_chance == 10:
                print("Miltank Missed Growl!")
                self.adaptiveString = "Miltank Missed Growl!"
            else:                                
                if player1_second_type == "":
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.stomp_type)
                    if state == "null":
                        print("Miltank Hit Growl!")
                        print("Doesn't Affect Enemy...")
                    else:
                        print("Miltank Hit Growl!")
                        self.player1Attack = player1_attack_stat * (1 - self.move) 
                else:
                    instance = Types.Types()
                    state = instance.typeLogic(player1_target_type, self.stomp_type) #Types.typeLogic(player1_target_type, self.tackle_type)
                    state2 = instance.typeLogic(player1_second_type, self.stomp_type)                   
                    if state == "null" or state2 == "null":
                        print("Miltank Hit Growl!")
                        print("Doesn't Affect Enemy...")
                    else:
                        print("Miltank Hit Growl!")
                        self.player1Attack = player1_attack_stat * (1 - self.move) 
            self.adaptiveString = "Miltank Hit Growl!"           
                                               
        elif rvalue == 3:
            #Fling
            self.move = self.fling * self.attack_stat
                                                   
            hit_chance = random.randrange(1,5)
            if hit_chance == 4:
                print("Miltank Missed Fling!")
                self.adaptiveString = "Miltank Missed Fling!"
            else:
                
                if player1_second_type == "":
                    temp = Types.Types() 
                    state = temp.typeLogic(player1_target_type, self.fling_type)
                    if state == "null":
                        print("Miltank Hit Fling!")
                        print("Doesn't Effect Enemy...")
                    elif state == "less":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * .5)
                        print("Miltank Hit Fling!")
                        print("Is not very effective...")
                        
                    elif state == "more":
                        self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * 1.5)
                        print("Miltank Hit Fling!")
                        print("Attack super effective!!")
                        
                    elif state == "same":
                        print("Miltank Hit Fling!")
                        self.player1Hp = player1_health - (self.move * (1 - (player1_defense_stat/100)))
                    
                else:
                    temp = Types.Types()
                    state = temp.typeLogic(player1_target_type, self.fling_type)
                    state2 = temp.typeLogic(player1_second_type, self.fling_type)
                    modifier = 1
                    modifier2 = 1
                    if state == "null" or state2 == "null":
                        print("Miltank Hit Fling!")
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
                        print("Miltank Hit Fling!")
                    elif modifier * modifier2 == 1/4:
                        print("Miltank Hit Fling!")
                        print("Is not very effective......")
                    elif modifier * modifier2 == 1/2:
                        print("Miltank Hit Fling!")
                        print("Is not very effective...")
                    elif modifier * modifier2 == 2:
                        print("Miltank Hit Fling!")
                        print("Attack super effective!!") 
                    elif modifier * modifier2 == 4:
                        print("Miltank Hit Fling!")
                        print("Attack super effective!!!!")                    
                    self.player1Hp = player1_health - ((self.move * (1 - (player1_defense_stat/100))) * (modifier * modifier2))
                self.adaptiveString = "Miltank Hit Fling!" 
                                               
        elif rvalue == 4:
            #Milkdrink - let me know if this one doesn't work - Kevin
            self.move = self.milk_drink
                                                   
            hit_chance = random.randrange(1,5)
            if hit_chance == 4:
                print("Miltank Missed Milkdrink!")
                self.adaptiveString = "Miltank Missed Milkdrink!"
            else:
                print("Miltank Hit Milkdrink!")
                self.adaptiveString = "Miltank Hit Milkdrink!"
                self.health = self.health + 30
                if self.health >= 95:
                    self.health = 95
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

        self.health = 145
        self.defense_stat = 45
        self.attack_stat = 45 
        

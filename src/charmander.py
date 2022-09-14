import pygame
import random
import time

class Charmander(pygame.sprite.Sprite):
        def __init__(self, x, y, img_file):
                """
                initializes the main Pokémon
                Args:
                        self (obj) - represents the Charmander object
                        x (int) - x coordinate of the upper left corner of the rectangle of the sprite
                        y (int) - y coordinate of the upper left corner of the rectangle of the sprite
                        img_file (string) - image representing the object
                Returns:
                        None
                """
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(img_file)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                #Charmander's stats
                self.health = 100
                self.attack_stat = 55
                self.defense_stat = 20 #Not dividing here will make the math easier for tail whip - Ant
                #Charmander's moves
                self.scratch = 30/100
                self.scratch_type = "normal"
                self.tail_whip = 50/100
                self.tail_whip_type = "normal"
                self.fire_fang = 80/100
                self.fire_fang_type = "fire"
                self.metal_claw = 60/100
                self.metal_claw_type = "steel"
                #Charmander's type
                self.main_type = "fire"
                self.second_type = "flying"
                #Names
                self.move1_name = "Scratch " #+ " (Type)" + self.scratch_type 
                self.move2_name = "Tail Whip " #+ " (Type)" + self.tail_whip_type 
                self.move3_name = "Fire Fang " #+ " (Type)" + self.fire_fang_type 
                self.move4_name = "Metal Claw " #+ " (Type)" + self.metal_claw_type 
                
                self.move = 0
                
                #Opponent Stats
                self.opponent_health = 0
                self.opponent_attack = 0
                self.opponent_defense = 0
                #self.opponent_type = oType
                #self.opponent_type2 = oType2
                
                #Text
                self.adaptiveString = ""
                self.name = "charmander"
                
        def attack(self, move_choice, opponent_health, opponent_attack, opponent_defense, opponent_type, opponent_type2):
                """
                Attacks the opposing Pokémon
                Args:
                        self (obj) - represents the Charmander object
                        move_choice
                        opponent_health (int) - health stat of the opposing pokémon
                        opponent_attack (int) - attack stat of the opposing pokémon
                        opponent_defense (int) - defense stat of the opposing pokémon
                        opponent_type
                        opponent_type2
                        
                Returns:
                        none    
                """
                #Test for remember method -Ant
                self.opponent_health = opponent_health
                self.opponent_attack = opponent_attack
                self.opponent_defense = opponent_defense
                
                #move_choice = int(input("input integer from range 1-4")) #Will replace with mouse key input once game loop is incorporated in controller - Just did it, Ant
                if move_choice == 1:
                        #Scratch           
                        self.move = self.scratch * self.attack_stat
                        hit_chance = random.randrange(1,11)
                        if hit_chance == 10:
                                print("Charmander Missed Scratch!")
                                self.adaptiveString = "Charmander Missed Scratch!"
                        else:
                                print("Charmander Hit Scratch!")
                                self.adaptiveString = "Charmander Hit Scratch!" 
                                self.opponent_health = opponent_health - (self.move * (1 - (opponent_defense/100)))
                                
                                
                elif move_choice == 2:
                        #Tail whip
                        self.move = self.tail_whip
                        hit_chance = random.randrange(1,11)
                        if hit_chance == 10:
                                print("Charmander Missed Tail Whip!")
                                self.adaptiveString = "Charmander Missed Tail Whip!"
                        else:
                                print("Charmander Hit Tail Whip!")
                                self.adaptiveString = "Charmander Hit Tail Whip!"
                                self.opponent_defense = opponent_defense * (1 - self.move)           
                                                      
                elif move_choice == 3:
                        #Fire Fang
                        self.move = self.fire_fang * self.attack_stat
                        hit_chance = random.randrange(1,3)
                        if hit_chance == 1:
                                print("Charmander Missed Fire Fang!")
                                self.adaptiveString = "Charmander Missed Fire Fang!"
                        else:
                                print("Charmander Hit Fire Fang!")
                                self.adaptiveString = "Charmander Hit Fire Fang!"
                                self.opponent_health = opponent_health - (self.move * (1 - (opponent_defense/100)))  
                                             
                elif move_choice == 4:
                        #Metal Claw
                        self.move = self.metal_claw * self.attack_stat                                        
                        hit_chance = random.randrange(1,5)
                        if hit_chance == 4:
                                print("Charmander Missed Metal Claw!")
                                self.adaptiveString = "Charmander Missed Metal Claw!"
                        else:
                                print("Charmander Hit Metal Claw!")
                                self.adaptiveString = "Charmander Hit Metal Claw!"
                                self.opponent_health = opponent_health - (self.move * (1 - (opponent_defense/100)))
                                
                                attack_raise_chance = random.randrange(1,3)
                                if attack_raise_chance == 1:
                                        print("Charmander Attack Rose!")
                                        self.adaptiveString = "Charmander Hit Metal Claw!(^)"
                                        self.attack_stat = self.attack_stat * (1.5) #Raising this by 50% should be fine, before it was 1 + 70/2 lol - Ant
                                        
                if self.opponent_health < 1:
                                        self.opponent_health = 0
       
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
                args: none
                returns none
                """

                self.health = 100
                self.defense_stat = 20
                self.attack_stat = 55 

import pygame
import random
import time

class Squirtle(pygame.sprite.Sprite):
        def __init__(self, x, y, img_file):
                """
                initializes the secondary Pokémon
                Args:
                        self (obj) - represents the Squirtle object
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
                #Squirtle's stats
                self.health = 120
                self.attack_stat = 40
                self.defense_stat = 30 #Not dividing here will make the math easier for tail whip - Ant
                #Squirtle's moves
                self.harden = 30/100
                self.harden_type = "normal"
                self.tackle = 40/100
                self.tackle_type = "normal"
                self.razorshell = 70/100
                self.razorshell_type = "water"
                self.hype = 35/100
                self.hype_type = "normal"
                #Squirtle's type
                self.main_type = "water"
                self.second_type = ""
                #Names
                self.move1_name = "Harden " #+ " (Type)" + self.headbutt_type 
                self.move2_name = "Tackle " #+ " (Type)" + self.tackle_type 
                self.move3_name = "Razor Shell " #+ " (Type)" + self.seed_bomb_type 
                self.move4_name = "Hype " #+ " (Type)" + self.force_palm_type 
                
                self.move = 0
                
                #Opponent Stats
                self.opponent_health = 0
                self.opponent_attack = 0
                self.opponent_defense = 0
                #self.opponent_type = oType
                #self.opponent_type2 = oType2
                 
                #Text
                self.adaptiveString = ""
                self.name = "squirtle"
                
        def attack(self, move_choice, opponent_health, opponent_attack, opponent_defense, opponent_type, opponent_type2):
                """
                Attacks the opposing Pokémon
                Args:
                        self (obj) - represents the Headbutt object
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
                        #Harden           
                        self.move = self.harden
                        hit_chance = random.randrange(1,11)
                        if hit_chance == 10:
                                print("Squirtle Missed Harden!")
                                self.adaptiveString = "Squirtle Missed Harden!"
                        else:
                                print("Squirtle Hit Harden!")
                                self.adaptiveString = "Squirtle Hit Harden! D(^)" 
                                self.defense_stat = self.defense_stat*(1+self.move)
                                if self.defense_stat > 80:
                                        self.defense_stat = 80
                                        self.adaptiveString = "Squirtle's is at max Defense!"
                                        
                                
                elif move_choice == 2:
                        #Tackle
                        self.move = self.tackle *self.attack_stat
                        hit_chance = random.randrange(1,11)
                        if hit_chance == 10:
                                print("Squirtle Missed Tackle!")
                                self.adaptiveString = "Squirtle Missed Tackle!"
                        else:
                                print("Squirtle Hit Tackle!")
                                self.adaptiveString = "Squirtle Hit Tackle!"
                                self.opponent_health = opponent_health - (self.move * (1 - (opponent_defense/100)))
                                                      
                elif move_choice == 3:
                        #Razor Shell
                        self.move = self.razorshell * self.attack_stat
                        hit_chance = random.randrange(1,5)
                        if hit_chance == 4:
                                print("Squirtle Missed Razor Shell!")
                                self.adaptiveString = "Squirtle Missed Razor Shell!"
                        else:
                                print("Squirtle Hit Razor Shell!")
                                self.adaptiveString = "Squirtle Hit Razor Shell!"
                                self.opponent_health = opponent_health - (self.move * (1 - (opponent_defense/100)))  
                                             
                elif move_choice == 4:
                        #Hype
                        self.move = self.hype                                        
                        hit_chance = random.randrange(1,10)
                        if hit_chance == 3:
                                print("Squirtle Missed Hype!")
                                self.adaptiveString = "Squirtle Missed Hype!"
                        else:
                                print("Squirtle Hit Hype!")
                                self.adaptiveString = "Squirtle Used Hype! A(^)"
                                self.attack_stat = self.attack_stat * (1+self.move)
                                if self.attack_stat > 80:
                                        self.attack_stat = 80
                                        self.adaptiveString = "Squirtle's is at max Attack!"
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
                args none
                returns none
                """

                self.health = 120
                self.defense_stat = 30
                self.attack_stat = 40
                

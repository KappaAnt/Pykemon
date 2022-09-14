import pygame
import sys
import random
import time
from pygame import mixer
import src.charmander
import src.bidoof
import src.actionMenu
import src.miltank
import src.squirtle
import src.rules

class Controller():                     #NOTE FOR VIEWER/TA/PROF
    def __init__(self):                 #If pikachu on the main menu moves extremely quick please change self.rate to 1/4 instead of 1 its speed is depends on how fast your machine is
        """
        Initializes the controller class vars and all the objects from other class models
        args: none
        returns: none
        """
        self.width = 825
        self.height = 800
        self.charX = -10
        self.charY = 205
        self.bidX = 550
        self.bidY = 100
        self.box1X = 375
        self.box2X = 600
        self.box1Y = 575
        self.box2Y = 685
        
        self.display = pygame.display.set_mode((self.width, self.height))
        self.main_mon = src.charmander.Charmander(self.charX, self.charY, "assets/charmanderback.png")
        self.sec_mon = src.squirtle.Squirtle(self.charX, self.charY, "assets/squirtle.png")
        self.charmander = self.main_mon #charmander represents main pokemon user is with
        #IF we want to switch pokemon add temp variable for the object for bidoof
        # self.temp_enemy = src.bidoof.Bidoof(self.bidX, self.bidY, "assets/bidoofpic.png") #self.bidoof = self.temp_enemy
        self.temp_enemy = src.miltank.Miltank(self.bidX, self.bidY, "assets/miltank.png")
        self.main_enemy = src.bidoof.Bidoof(self.bidX, self.bidY, "assets/bidoofpic.png") 
        self.bidoof = self.main_enemy #bidoof is weirdly not supposed to represent the pokemon but the enemy instance            
        self.moves1 = src.actionMenu.actionMenu(self.box1X, self.box1Y, "assets/moveRectangle.png", 1)
        self.moves2 = src.actionMenu.actionMenu(self.box2X, self.box1Y, "assets/moveRectangle.png", 2)
        self.moves3 = src.actionMenu.actionMenu(self.box1X, self.box2Y, "assets/moveRectangle.png", 3)
        self.moves4 = src.actionMenu.actionMenu(self.box2X, self.box2Y, "assets/moveRectangle.png", 4)

        pygame.font.init()
        #Font Init
        self.font = pygame.font.SysFont(None, 30)
        self.font2 = pygame.font.SysFont(None, 25)
        #End Display
        #self.end_display = pygame.display.set_mode((self.width, 465))
        self.end_image = pygame.image.load("assets/end.jpg") # 825, 465
        #Intro Display
        #self.intro_display = pygame.display.set_mode((self.width, self.height))
        self.intro_image = pygame.image.load("assets/mainmenu.png")
        self.intro_party1 = pygame.image.load("assets/pika1.png")
        self.intro_party2 = pygame.image.load("assets/pika2.png")
        

        self.random = random.randrange(1,3)
        self.random2 = random.randrange(1,3)
        self.random3 = random.randrange(1,3)
        
        if self.random3 == 1:
            self.background_image = pygame.image.load("assets/background2.jpg")
        elif self.random3 ==2:
            self.background_image = pygame.image.load("assets/bluegrass.png")
               
        self.background_image2 = pygame.image.load("assets/newmenu.png") 
        
        
        self.condition = False #For Moves
        self.condition2 = True #Intro Screen
        self.condition3 = True #Batte Music
        self.condition4 = False #End Screen
        self.condition5 = True #Intro Music
        self.condition6 = True #End Music
        self.condition7 = True #Enemy switching
        self.condition8 = True #Partner switching
        self.condition9 = True #Json File
        self.flexX_1 = random.randrange(0,200)*-1
        self.flexX_R1 = random.randrange(650,750)
        self.flexY_1 = random.randrange(0,200)*-1
        self.flexY_R1 = random.randrange(650,750)*-1
        self.flexX_2 = self.width + random.randrange(0,200)
        self.flexX_R2 = self.width + random.randrange(500,600)
        self.flexY_2 = random.randrange(0,200)*-1
        self.flexY_R2 = random.randrange(500,600)*-1
        self.midX = -100
        self.midY = random.randrange(0,800)
        self.midXR = 900
        self.midYR = random.randrange(0,800)
        
        self.more = 100
        self.rate = 1
        self.temp = 0
        self.STATE = "game"
        
        self.json = src.rules.Rules()  # JSON OBJ
        
        #For text
        self.defaultString = "What will " + self.charmander.name + " do?"
        
    def mainLoop(self):
        """
        mainLoop handles two sides of the coin; continuing or ending the game by running the gameLoop and preparing for an exitLoop
        args:none
        returns: none
        """
        while True:
            if self.STATE == "game":
                self.gameLoop()
            elif self.STATE == "exit":
                self.exitLoop()
            
    def gameLoop(self):
        """
        gameLoop for the graphics, handle all events, displays the GUI and covers turn based combat
        args: none
        returns: none
        """
        while self.STATE == "game":
            #Intro Music
            
            if self.condition5 == True:
                if self.random == 1:
                    mixer.music.load("assets/m1music.mp3")
                elif self.random == 2:
                    mixer.music.load("assets/menu2.mp3")     
                mixer.music.play(-1)
                self.condition5 = False
                
                
            while self.condition2 == True:
                self.display.blit(self.intro_image, (0,0))
                #Text for options
                m1 = self.font.render("Press Space To Play", False, (0,0,0))
                center = m1.get_rect(center=(self.width/2, self.height/2))
                self.display.blit(m1, center)
                m2 = self.font.render("Press Esc for Info/Data", False, (0,0,0))
                center2 = m2.get_rect(center=(self.width/2, (self.height-self.more)/2))
                self.display.blit(m2, center2)
                #Party Sprites
                #From Top Left
                self.display.blit(self.intro_party2, (self.flexX_1,self.flexY_1))
                self.display.blit(self.intro_party2, (self.flexX_R1,self.flexY_R1))
                #From Top Right
                self.display.blit(self.intro_party1, (self.flexX_2,self.flexY_2))
                self.display.blit(self.intro_party1, (self.flexX_R2,self.flexY_R2))
                #Middle Zag
                #self.intro_display.blit(self.intro_party2, (self.midX, self.midY))
                #self.intro_display.blit(self.intro_party1, (self.midXR, self.midYR))
            
                #TL
                if self.flexX_1 < (self.width+self.more):
                    self.flexX_1 += self.rate
                    self.flexY_1 += self.rate
                elif self.flexX_1 == (self.width+self.more):
                    self.flexX_1 = random.randrange(75,200)*-1
                    self.flexY_1 = random.randrange(75,200)*-1
                if self.flexX_R1 < (self.width+self.more):
                    self.flexX_R1 += self.rate
                    self.flexY_R1 += self.rate
                elif self.flexX_R1 == (self.width+self.more):
                    self.flexX_R1 = random.randrange(500,750)*-1
                    self.flexY_R1 = random.randrange(500,750)*-1
                #TR
                if self.flexY_2 < (self.width+self.more):
                    self.flexX_2 -= self.rate
                    self.flexY_2 += self.rate
                elif self.flexY_2 == (self.width+self.more):
                    self.flexX_2 = random.randrange(800,1000)
                    self.flexY_2 = random.randrange(75,200)*-1
                if self.flexY_R2 < (self.width+self.more):
                    self.flexX_R2 -= self.rate
                    self.flexY_R2 += self.rate
                elif self.flexY_R2 == (self.width+self.more):
                    self.flexX_R2 = random.randrange(1000,1200)
                    self.flexY_R2 = random.randrange(500,750)*-1
                #MZ
                """
                if self.midX < (self.width+self.more):
                    self.midX += self.rate
                    if self.midX < 100:
                        self.midY += self.rate
                    elif self.midX < 200:
                        self.midY -=self.rate
                    elif self.midX < 300:
                        self.midY +=self.rate
                    elif self.midX < 400:
                        self.midY -=self.rate
                    elif self.midX < 500:
                        self.midY +=self.rate
                    elif self.midX < 600:
                        self.midY -=self.rate
                    elif self.midX < 700:
                        self.midY +=self.rate
                    elif self.midX < 800:
                        self.midY -=self.rate
                    elif self.midX < 900:
                        self.midY +=self.rate
                    elif self.midX == 900:
                        self.midX = (self.more+self.more+self.more+self.more)*-1
                        self.midY = random.randrange(0,500)
                        
                if self.midXR > -self.more:
                    self.midXR -= self.rate
                    if self.midXR > 900:
                        self.midYR += self.rate
                    elif self.midXR > 800:
                        self.midYR -=self.rate
                    elif self.midXR > 700:
                        self.midYR +=self.rate
                    elif self.midXR > 600:
                        self.midYR -=self.rate
                    elif self.midXR > 500:
                        self.midYR +=self.rate
                    elif self.midXR > 400:
                        self.midYR -=self.rate
                    elif self.midXR > 300:
                        self.midYR +=self.rate
                    elif self.midXR > 200:
                        self.midYR -=self.rate
                    elif self.midXR > 100:
                        self.midYR +=self.rate
                    elif self.midXR > 0:
                        self.midYR -=self.rate
                    elif self.midXR > -100:
                        self.midYR +=self.rate
                    elif self.midXR == -100:
                        self.midXR = self.width+self.more+self.more+self.more+self.more
                        self.midYR = random.randrange(0,500)
                    """#Another pika sprite but it lags my vm too much
                
                #Event handler for First Menu
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.STATE = "exit"
                        self.condition2 = False
                    if event.type == pygame.KEYDOWN:
                        if event.key ==  pygame.K_SPACE:
                            self.condition2 = False
                            mixer.music.stop()
                        elif event.key ==  pygame.K_ESCAPE:
                            while self.condition9 == True:
                                self.display.fill((192, 191, 191))
                                #Info screen text, dealing with JSON
                                m3 = self.font2.render(str(self.json.menu_list[0]), False, (0,0,0))
                                self.display.blit(m3, (0,100))
                                m4 = self.font2.render(str(self.json.menu_list[1]), False, (0,0,0))
                                self.display.blit(m4, (0,125))
                                m5 = self.font2.render(str(self.json.menu_list[2]), False, (0,0,0))
                                self.display.blit(m5, (0,150))
                                m6 = self.font2.render(str(self.json.menu_list[3]), False, (0,0,0))
                                self.display.blit(m6, (0,175))
                                m6c = self.font2.render(str(self.json.menu_list[7]), False, (0,0,0))
                                self.display.blit(m6c, (0,200))
                                m7 = self.font2.render(str(self.json.menu_list[4]), False, (0,0,0))
                                self.display.blit(m7, (0,225))
                                m7c = self.font2.render(str(self.json.menu_list[8]), False, (0,0,0))
                                self.display.blit(m7c, (0,250))
                                m8 = self.font2.render(str(self.json.menu_list[5]), False, (0,0,0))
                                self.display.blit(m8, (0,275))
                                m8c = self.font2.render(str(self.json.menu_list[9]), False, (0,0,0))
                                self.display.blit(m8c, (0,300))
                                m9 = self.font2.render(str(self.json.menu_list[6]), False, (0,0,0))
                                self.display.blit(m9, (0,325))
                                m9c = self.font2.render(str(self.json.menu_list[10]), False, (0,0,0))
                                self.display.blit(m9c, (0,350))
                                m = self.font.render("Press Esc to Exit", False, (0,0,0))
                                self.display.blit(m, (0,0))
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        self.STATE = "exit"
                                        self.condition9 = False
                                        self.condition2 = False
                                    if event.type == pygame.KEYDOWN:
                                        if event.key ==  pygame.K_ESCAPE:
                                            self.condition9 = False
                                            
                                pygame.display.flip()
                self.condition9 = True                
                pygame.display.flip()

            #Battle music 
            if self.condition3 == True:
                if self.random2 == 1:
                    mixer.music.load("assets/menu3.mp3")
                elif self.random2 == 2:      
                    mixer.music.load("assets/battle.mp3")
                mixer.music.play(-1)
                self.condition3 = False
                

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.STATE = "exit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.moves1.rect.collidepoint(event.pos)):
                        self.charmander.attack(self.moves1.move_choice, self.bidoof.health, self.bidoof.attack_stat, self.bidoof.defense_stat, self.bidoof.main_type, self.bidoof.second_type)
                        #Charmander scratch text
                        self.temp = 1
                        self.condition = True
                    elif(self.moves2.rect.collidepoint(event.pos)):
                        self.charmander.attack(self.moves2.move_choice, self.bidoof.health, self.bidoof.attack_stat, self.bidoof.defense_stat, self.bidoof.main_type, self.bidoof.second_type)
                        
                        self.temp = 2
                        self.condition = True
                    elif(self.moves3.rect.collidepoint(event.pos)):
                        self.charmander.attack(self.moves3.move_choice, self.bidoof.health, self.bidoof.attack_stat, self.bidoof.defense_stat, self.bidoof.main_type, self.bidoof.second_type)
                        self.temp = 3
                       
                        self.condition = True
                    elif(self.moves4.rect.collidepoint(event.pos)):
                        self.charmander.attack(self.moves4.move_choice, self.bidoof.health, self.bidoof.attack_stat, self.bidoof.defense_stat, self.bidoof.main_type, self.bidoof.second_type)
                        self.temp = 4
                        
                        self.condition = True
                    
                    if self.condition == True:
                        self.bidoof.remember(self.charmander.opponent_health,self.charmander.opponent_defense,self.charmander.opponent_attack)
                        self.bidoof.attack(self.charmander.health, self.charmander.defense_stat, self.charmander.attack_stat, self.charmander.main_type, self.charmander.second_type)
                        self.charmander.remember(self.bidoof.player1Hp, self.bidoof.player1Defense, self.bidoof.player1Attack)
                        self.condition = False   
                            

            #Adding a background for battle
            self.display.fill((192, 192, 192))
            self.display.blit(self.background_image, (0, 0))
            self.display.blit(self.background_image2, (0, 535))
            #Charmander Text Draft
            #Question Text
            if self.temp == 0: #question
                nameQuestion = self.font.render(str(self.defaultString), False, (0,0,0))
                self.display.blit(nameQuestion, (30, 585))
            elif self.temp == 1: #scratch
                self.display.blit(self.background_image2, (0, 535))
                adaptiveText = self.font.render(self.charmander.adaptiveString, False, (0,0,0))
                self.display.blit(adaptiveText, (30, 585))
            elif self.temp == 2: #tail
                self.display.blit(self.background_image2, (0, 535))
                adaptiveText = self.font.render(self.charmander.adaptiveString, False, (0,0,0))
                self.display.blit(adaptiveText, (30, 585))
            elif self.temp == 3: #fire
                self.display.blit(self.background_image2, (0, 535))
                adaptiveText = self.font.render(self.charmander.adaptiveString, False, (0,0,0))
                self.display.blit(adaptiveText, (30, 585))
            elif self.temp == 4: #metal
                self.display.blit(self.background_image2, (0, 535))
                adaptiveText = self.font.render(self.charmander.adaptiveString, False, (0,0,0))
                self.display.blit(adaptiveText, (30, 585))
                
            #Bidoof Text
            bidoofText = self.font.render(self.bidoof.adaptiveString, False, (0,0,0))
            self.display.blit(bidoofText, (30, 605))
                
                
            #Drawing the screen
            
            #Player 1 HP
            self.display.blit(self.charmander.image, (self.charmander.rect.x, self.charmander.rect.y))           
            player1HP = self.font.render("HP: " + str(int(self.charmander.health)), False, (0,0,0))
            self.display.blit(player1HP, (50, 230+75))                      
            #Enemy HP                        
            self.display.blit(self.bidoof.image, (self.bidoof.rect.x, self.bidoof.rect.y))
            player2HP = self.font.render("HP: " + str(int(self.bidoof.health)), False, (0,0,0))
            self.display.blit(player2HP, (550, 70))  
            #Move Boxes
            self.display.blit(self.moves1.image, (self.moves1.rect.x, self.moves1.rect.y))
            self.display.blit(self.moves2.image, (self.moves2.rect.x, self.moves2.rect.y))
            self.display.blit(self.moves3.image, (self.moves3.rect.x, self.moves3.rect.y))
            self.display.blit(self.moves4.image, (self.moves4.rect.x, self.moves4.rect.y))
            #Move Names
            m1 = self.font.render(self.charmander.move1_name, False, (0,0,0))
            self.display.blit(m1, (self.box1X+30, self.box1Y+30))
            m2 = self.font.render(self.charmander.move2_name, False, (0,0,0))
            self.display.blit(m2, (self.box2X+30, self.box1Y+30))
            m3 = self.font.render(self.charmander.move3_name, False, (0,0,0))
            self.display.blit(m3, (self.box1X+30, self.box2Y+30))
            m4 = self.font.render(self.charmander.move4_name, False, (0,0,0))
            self.display.blit(m4, (self.box2X+30, self.box2Y+30))
            pygame.display.flip()

            
            if self.bidoof.health == 0:
                if self.condition7 == True:
                    self.bidoof.reset() #let the dead bidoof regain stats so this cycle will work, but only for main enemy
                    self.condition7 = False
                    self.bidoof = self.temp_enemy
                #Game End Screen
                if self.bidoof.health == 0:
                    self.condition4 = True            
                    mixer.music.stop()
                    while(self.condition4 == True):
                        self.display.fill((192, 192, 191))
                        self.display.blit(self.end_image, (0,0))
                        m1 = self.font.render("Press Escape To Exit", False, (252,252,252))
                        m2 = self.font.render("You Won!!!", False, (252,252,252))
                        m3 = self.font.render("Press Space To Play Again", False, (252,252,252))
                        center = m1.get_rect(center=(self.width/2, 465/2))
                        center2 = m2.get_rect(center=(self.width/2, self.more/2))
                        center3 = m3.get_rect(center=(self.width/2, (self.more+self.more)/2))
                        self.display.blit(m1, center)
                        self.display.blit(m2, center2)
                        self.display.blit(m3, center3)
                        if self.condition6 == True:
                            mixer.music.load("assets/win.mp3")          
                            mixer.music.play(-1)
                            self.condition6 = False 
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.condition4 = False
                                self.STATE = "exit"                           
                            if event.type == pygame.KEYDOWN:
                                if event.key ==  pygame.K_ESCAPE:
                                    self.condition4 = False
                                    self.STATE = "exit"
                                elif event.key ==  pygame.K_SPACE:
                                    self.condition2 = True #Intro Screen
                                    self.condition3 = True #Battle Music
                                    self.condition4 = False #End Screen
                                    self.condition5 = True #Intro Music
                                    self.condition6 = True #End Music
                                    self.condition7 = True #For cycle
                                    self.condition8 = True #For partner cycle
                                    self.condition9 = True #For Data Info
                                    self.random = random.randrange(1,3) #For Intro Music
                                    #I need a reset stat method
                                    self.charmander.reset()
                                    self.bidoof.reset()
                                    #Set back to main enemy/partner
                                    self.bidoof = self.main_enemy
                                    self.charmander = self.main_mon
                        pygame.display.flip()
                                      
               
            elif self.charmander.health == 0:
                if self.condition8 == True:
                    self.charmander.reset() #let the dead charmander reset stats but switch to squirtle.
                    self.condition8 = False
                    self.charmander = self.sec_mon
                #Game End Screen but good
                if self.charmander.health == 0:
                    self.condition4 = True            
                    mixer.music.stop()
                    while(self.condition4 == True):
                        self.display.fill((192, 192, 191))
                        self.display.blit(self.end_image, (0,0))
                        m1 = self.font.render("Press Escape To Exit", False, (252,252,252))
                        m2 = self.font.render("You Lost!!!", False, (252,252,252))
                        m3 = self.font.render("Press Space To Play Again", False, (252,252,252))
                        center = m1.get_rect(center=(self.width/2, 465/2))
                        center2 = m2.get_rect(center=(self.width/2, self.more/2))
                        center3 = m3.get_rect(center=(self.width/2, (self.more+self.more)/2))
                        self.display.blit(m1, center)
                        self.display.blit(m2, center2)
                        self.display.blit(m3, center3)
                        if self.condition6 == True:
                            mixer.music.load("assets/loss.mp3")          
                            mixer.music.play(-1)
                            self.condition6 = False 
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.condition4 = False
                                self.STATE = "exit"                           
                            if event.type == pygame.KEYDOWN:
                                if event.key ==  pygame.K_ESCAPE:
                                    self.condition4 = False #End Screen 
                                    self.STATE = "exit"
                                elif event.key ==  pygame.K_SPACE:
                                    #Resetting stuff to allow gameLoop to function originally
                                    self.condition2 = True #Intro Screen
                                    self.condition3 = True #Battle Music
                                    self.condition4 = False #End Screen
                                    self.condition5 = True #Intro Music
                                    self.condition6 = True #End Music
                                    self.condition7 = True #For enemy cycle
                                    self.condition8 = True #For cycle
                                    self.condition9 = True #For Data Info
                                    self.random = random.randrange(1,3) #For Intro Music
                                    #I need a reset stat method
                                    self.charmander.reset()
                                    self.bidoof.reset()
                                    #Set back to main enemy/partner
                                    self.bidoof = self.main_enemy
                                    self.charmander = self.main_mon
                                                            
                        pygame.display.flip()
                     
                        
                              
    def exitLoop(self):
        """
        exitLoop, counterpart of gameLoop; will stop the game from running and close application
        args: none
        returns: none
        """
        pygame.quit()
        exit()


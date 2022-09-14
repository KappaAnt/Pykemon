import pygame
#import requests #if this causes you an error type "pip3 install requests" in cmd

#Ant here, because im going to have to do the controller, which i am not confident about.
#I am making sure every model we have can be worked with, so im going to try to get move options to be functional here.

class actionMenu(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, move_choice): 
        """
        Initializes action menu vars
        args: x,y,img_file,move_choice
        returns: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha() 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_choice = move_choice
        
import pygame
from src import controller

def main():
    pygame.init()
    #Team
    print("Lead and Frontend is: Anthony Albanese")
    print("Backend is: Kyle Enriquez")    
    #Create an instance on your controller object
    game = controller.Controller()
    game.mainLoop()
    
main()

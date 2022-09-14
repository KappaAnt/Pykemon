import random

class Types():
    def __init__(self):
        """
        Initialization for Types. The system works but was not fully implemented into the game for balance and time issues
        args: none
        returns none
        """
        
        self.fire = "fire"
        self.normal = "normal"
        self.dark = "dark"
        self.bug = "bug"
        self.dragon = "dragon"
        self.electric = "electric"
        self.fighting = "fighting"
        self.flying = "flying"
        self.ghost = "ghost"
        self.grass = "grass"
        self.ground = "ground"
        self.ice = "ice"
        self.poison = "poison"
        self.psychic = "pyschic"
        self.rock = "rock"
        self.water = "water"
        self.steel = "steel"
        
    def typeLogic(self, target_type, move_type):
        """
        Allows for a type system with supereffective/ineffective attacks
        args: target_type and move_type
        returns: less or more or same or null
        """

        if target_type == self.fire:
            if move_type == self.fire:
                #Ineffective
                return "less"
            elif move_type == self.grass:
                #Ineffective
                return "less"
            elif move_type == self.ice:
                #Ineffective
                return "less"
            elif move_type == self.steel:
                #Ineffective
                return "less"
            elif move_type == self.water:
                #SuperEffective
                return "more"
            elif move_type == self.ground:
                #SuperEffective
                return "more"
            elif move_type == self.rock:
                #SuperEffective
                return "more"
            else:
                #Normal
                return "same"                                
        elif target_type == self.normal:
            if move_type == self.fighting:
                #SuperEffective
                return "more"
            elif move_type == self.ghost:
                #NoEffect
                return "null"
            else:
                #Normal
                return "same"                
        elif target_type == self.dark:
            if move_type == self.fighting:
                #SuperEffective
                return "more"
            elif move_type == self.bug:
                #SuperEffective
                return "more"
            elif move_type == self.psychic:
                #Null
                return "null"
            elif move_type == self.ghost:
                #Ineffective
                return "less"
            elif move_type == self.dark:
                #Ineffective
                return "less"
            else:
                #Normal
                return "same"
        elif target_type == self.bug: #I think you get the comments
            if move_type == self.fire:
                return "more"
            elif move_type == self.flying:
                return "more"
            elif move_type == self.rock:
                return "more"
            elif move_type == self.grass:
                return "less"
            elif move_type == self.fighting:
                return "less"
            elif move_type == self.ground:
                return "less"
            else:
                return "same"
        elif target_type == self.dragon:
            if move_type == self.fire:
                return "less"
            elif move_type == self.water:
                return "less"
            elif move_type == self.electric:
                return "less"
            elif move_type == self.grass:
                return "less"
            elif move_type == self.ice:
                return "more"
            elif move_type == self.dragon:
                return "more"
            else:
                return "same"
        elif target_type == self.electric:
            if move_type == self.ground:
                return "more"
            elif move_type == self.flying:
                return "less"
            elif move_type == self.electric:
                return "less"
            elif move_type == self.steel:
                return "less"
            else:
                return "same"
        elif target_type == self.fighting:
            if move_type == self.flying:
                return "more"
            elif move_type == self.psychic:
                return "more"
            elif move_type == self.bug:
                return "less"
            elif move_type == self.rock:
                return "less"
            elif move_type == self.dark:
                return "less"
            else:
                return "same"
        elif target_type == self.flying:
            if move_type == self.electric:
                return "more"
            elif move_type == self.ice:
                return "more"
            elif move_type == self.rock:
                return "more"
            elif move_type == self.grass:
                return "less"
            elif move_type == self.fighting:
                return "less"
            elif move_type == self.bug:
                return "less"
            elif move_type == self.ground:
                return "null"
            else:
                return "same"
        elif target_type == self.ghost:
            if move_type == self.dark:
                return "more"
            elif move_type == self.ghost:
                return "more"
            elif move_type == self.bug:
                return "less"
            elif move_type == self.poison:
                return "less"
            elif move_type == self.fighting:
                return "null"
            elif move_type == self.normal:
                return "null"
            else:
                return "same"       
        elif target_type == self.grass:
            if move_type == self.fire:
                return "more"
            elif move_type == self.ice:
                return "more"
            elif move_type == self.poison:
                return "more"
            elif move_type == self.flying:
                return "more"
            elif move_type == self.bug:
                return "more"
            elif move_type == self.water:
                return "less"
            elif move_type == self.electric:
                return "less"
            elif move_type == self.grass:
                return "less"
            elif move_type == self.ground:
                return "less"
            else:
                return "same"
        elif target_type == self.ground:
            if move_type == self.water:
                return "more"
            elif move_type == self.grass:
                return "more"
            elif move_type == self.ice:
                return "more"
            elif move_type == self.poison:
                return "less"
            elif move_type == self.rock:
                return "less"
            elif move_type == self.electric:
                return "null"
            else:
                return "same"  
        elif target_type == self.ice:
            if move_type == self.fire:
                return "more"
            elif move_type == self.fighting:
                return "more"
            elif move_type == self.ice:
                return "less"
            elif move_type == self.poison:
                return "less"
            elif move_type == self.rock:
                return "more"
            elif move_type == self.steel:
                return "more"
            else:
                return "same"
        elif target_type == self.poison:
            if move_type == self.ground:
                return "more"
            elif move_type == self.psychic:
                return "more"
            elif move_type == self.grass:
                return "less"
            elif move_type == self.fighting:
                return "less"
            elif move_type == self.poison:
                return "less"
            elif move_type == self.bug:
                return "less"
            else:
                return "same"
        elif target_type == self.psychic:
            if move_type == self.bug:
                return "more"
            elif move_type == self.ghost:
                return "more"
            elif move_type == self.dark:
                return "more"
            elif move_type == self.psychic:
                return "less"
            elif move_type == self.fighting:
                return "less"
            else:
                return "same"
        elif target_type == self.rock:
            if move_type == self.water:
                return "more"
            elif move_type == self.grass:
                return "more"
            elif move_type == self.fighting:
                return "more"
            elif move_type == self.ground:
                return "more"
            elif move_type == self.steel:
                return "more"
            elif move_type == self.normal:
                return "less"
            elif move_type == self.fire:
                return "less"
            elif move_type == self.poison:
                return "less"
            elif move_type == self.flying:
                return "less"
            else:
                return "same"
        elif target_type == self.water:   #THIS TOOK A LONG TIME 
            if move_type == self.electric:
                return "more"
            elif move_type == self.grass:
                return "more"
            elif move_type == self.fire:
                return "less"
            elif move_type == self.water:
                return "less"
            elif move_type == self.ice:
                return "less"
            elif move_type == self.steel:
                return "less"
            else:
                return "same"
            
            

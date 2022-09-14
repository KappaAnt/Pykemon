import json

class Rules:
        def __init__(self):
                """
                Initializer for Rules Class, reads json file and makes json object
                args: none
                returns: none
                """
                #menu_list = []                                 #Earlier method used, not needed anymore - Kyle 
                #for pokemon_obj in open("pokemon.json"):
                        #pokemon_dict = json.loads(pokemon_obj)
                        #menu_list.append(pokemon_dict)
                self.fileref = open("src/pokemon.json", "r")
                self.menu_list = json.load(self.fileref)
                #with open("pokemon.json", "r") as self.fileref:
                        #self.menu_list = json.load(self.fileref)    
                #self.pretty_json = json.dumps(self.menu_list, indent = 4)

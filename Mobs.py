import os

class Mobs:
    def __init__(self, name,hp, atk, drop):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.item_drop = drop
    
    def display_status(self):
        os.system("cls")
        print("=========================")
        print(">> ",self.name)
        print()
        print("HP:",self.hp,"",)
        print("ATK:",self.atk)
        print()
        print("=========================")
        input("press any key to continue...")

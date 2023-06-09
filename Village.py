from Steve import *
from random import randint
import os

with open("C:\\Users\\smart\\OneDrive\\Documents\\GitHub\\text_based-game_project\\Item_Ability.json", "r") as read_file:
    item_ablt = load(read_file)


def farming():
    os.system("cls")
    if steve.already_farming:
        print("You already helping the villager.")
        input("press any key to continue...")
        return
    
    
    steve.already_farming = True
    #chance drop
    random = randint(1,100)
    quantity = randint(2,5)
    if random >= 1  and  random < 26:
        food = "apple"
    elif random >= 26 and random < 51:
        food = "carrot"
    elif random >= 51 and random < 76:
        food = "potato"
    else:
        food = "bread"
        
    for i in range(quantity):
        added_check = steve.add_item(food)
        if not added_check:
            quantity = i+1
            break
    print("You have obtained",food,"for",quantity,"pieces")
    input("press any key to continue...")
    
    

def upgrade():
    os.system("cls")
    
    if "diamond" in steve.invt:
        for i in item_ablt["upgrade_item"]["diamond"]:
            steve.add_item(i)
        input("Your upgraded sword and pickaxe has been added!!")
        
    elif "iron" in steve.invt:
        for i in item_ablt["upgrade_item"]["iron"]:
            steve.add_item(i)
        input("Your upgraded sword and pickaxe has been added!!")
        
    elif "stone" in steve.invt:
        for i in item_ablt["upgrade_item"]["stone"]:
            steve.add_item(i)
        input("Your upgraded sword and pickaxe has been added!!")
        
    else :
        input("There is nothing to upgrade...")

def eating():
    os.system("cls")
    
    if(steve.hp == 20):
        print("Your health is already full")
        input("press any key to continue...")
        return
    
    print("HP : ",steve.hp,"/ 20")
    print("What do you want to eat")
    food = input(">> ")
    if food not in steve.invt:
        print("You don't have this food...")
        input("press any key to continue...")
        return
    
    steve.healed(food)
    print("HP : ",steve.hp,"/ 20")
    input("press any key to continue...")
    
    
def menu(go_dungeon):
    os.system("cls")
    print("==================================")
    print("Take a rest before exploring again")
    print("1) Eating")
    print("2) Upgrade")
    print("3) Farming")
    print("4) Check inventory")
    print("5) Check Status")
    print("6) Exploring Dungeon")
    print("==================================")
    
    choice = "0" 
    while choice not in ["1","2","3","4","5","6"]:
        choice = input(">> ")
        
        if choice == "1" :
            eating()
        elif choice == "2":
            upgrade()
        elif choice == "3":
            farming()
        elif choice == "4":
            steve.display_invt()
        elif choice == "5":
            steve.display_status()
        elif choice == "6":
            go_dungeon = True
    return go_dungeon
        

   
# main sequence


def village_scene():
    steve.already_farming = False
    go_dungeon = False
    input("Welcome to Village")
    while go_dungeon == False:
        
        go_dungeon = menu(go_dungeon)
        
    os.system("cls")
    input("Goodluck..")
    return
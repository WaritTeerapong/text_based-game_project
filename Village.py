from Steve import *
from random import randint

go_dungeon = False
already_farming = False

def farming():
    if already_farming:
        print("You already helping the villager.")
        return
    
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
    
    

# def crafting():
#     pass

def eating():
    pass

def menu():
    print("==================================")
    print("Take a rest before exploring again")
    print("1) Eating")
    print("2) Farming")
    print("3) Check inventory")
    print("4) Check Status")
    print("5) Exploring Dungeon")
    print("==================================")
    
    choice = 0 
    while choice not in [1,2,3,4,5]:
        choice = int(input(">> "))
        
        if choice == 1 :
            eating()
        elif choice == 2:
            farming()
        elif choice == 3:
            steve.display_invt()
        elif choice == 4:
            steve.display_status()
        elif choice == 5:
            go_dungeon = True
        
        
    


   
# main sequence
def village_scene():
    print("Welcome to Village")
    while go_dungeon == False:

        menu()
    
    print("Goodluck..")
    return
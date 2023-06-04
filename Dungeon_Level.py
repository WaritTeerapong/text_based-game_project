from Steve import *
from random import randint
import Mobs

with open("C:\\Users\\smart\\OneDrive\\Documents\\GitHub\\text_based-game_project\\Level_info.json", "r") as read_file:
    lvl_info = load(read_file)

with open("C:\\Users\\smart\\OneDrive\\Documents\\GitHub\\text_based-game_project\\Item_Ability.json", "r") as read_file:
    item_ablt = load(read_file)
    

def fight_mobs():
    pass

def found_ore(lv):
    ore = lvl_info[lv]["ore"]
    
    pickaxe = steve.search_pickaxe()
    if ore in item_ablt["mining_item"][pickaxe]:
        os.system("cls")
        print("============================")
        print()
        print("Congratulations!!!")
        print("You have found",ore,"!!!")
        print()
        print("============================")
        input("Press any key to continue...")
    else:
        os.system("cls")
        print("============================")
        print()
        print("Unfortunately... your pickaxe is not strong enough")
        print("You can UPGRADE at the village")
        print()
        print("============================")
        input("Press any key to continue...")
        
        os.system("cls")
    


def lv_1():
    # ore_chance = 50
    # mob_chance = 50
    
    if randint(1,100) <= 50:
        found_ore()
    else:
        fight_mobs()
        

def lv_2():
    # ore_chance = 30
    # mob_chance = 70
    if randint(1,100) <= 30:
        found_ore()
    else:
        fight_mobs()

def lv_3():
    # ore_chance = 10
    # mob_chance = 90
    if randint(1,100) <= 10:
        found_ore()
    else:
        fight_mobs()



def next_level(current_level):
    
    if current_level == "1":
        lv_1()
    elif current_level == "2":
        lv_2()
    elif current_level == "3":
        lv_3()

# main sequence
def dungeon_scene():
    exit_dungeon = False
    level = 0
    choice = "0" 
    
    while exit_dungeon == False:
        if level>0:
            os.system("cls")
            print("Would you like to go deeper or back to village")
            print("1) continue exploring")
            print("2) back to village")
            choice = input(">> ")
            if choice == "1" :
                pass
            elif choice == "2":
                input("you are exiting dungeon...")
                exit_dungeon = True
            
            while choice not in ["1","2"]:
                choice = input(">> ")
                if choice == "1" :
                    break
                elif choice == "2":
                    os.system("cls")
                    input("you are exiting dungeon...")
                    exit_dungeon = True
                    
        #exit dungeon
        if exit_dungeon: 
            break
        level += 1            
        next_level(level)
              
        
        
        
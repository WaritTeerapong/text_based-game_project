from Steve import *
from Mobs import *
from random import randint
from Village import eating


with open("C:\\Users\\smart\\OneDrive\\Documents\\GitHub\\text_based-game_project\\Level_info.json", "r") as read_file:
    lvl_info = load(read_file)

with open("C:\\Users\\smart\\OneDrive\\Documents\\GitHub\\text_based-game_project\\Item_Ability.json", "r") as read_file:
    item_ablt = load(read_file)

def flee(exit_dungeon):
    os.system("cls")
    input("You felt unready to counter such a powerful monster")
    input("and took some hit when trying to run away...")
    steve.hp -= 10
    os.system("cls")
    input("You are going back to the village")
    exit_dungeon = True
    return exit_dungeon
    
def fight(lv,exit_dungeon,mob):
    weapon = steve.search_sword()
    if item_ablt["attack_item"][weapon] >= lv:
        os.system("cls")
        print("============================")
        print()
        print("You defeat",mob.name,"!!!")
        print()
        print("============================")
        mob.hp = 0
        steve.hp -= mob.atk
        input()
        steve.display_status()
        
        os.system("cls")
        print("============================")
        print()
        print("Congratulations!!!")
        print("You obtain",mob.item_drop,"from the monster!!!")
        print()
        print("============================")
        input("Press any key to continue...")
        steve.add_item(mob.item_drop)
        
        exit_dungeon = False
    
    else:
        os.system("cls")
        input("Your system was not stong enough to take down the monster...")
        input("You are defeated..")
        os.system("cls")
        input("You are going back to the village")
        steve.hp = 1
        exit_dungeon = True
        
    return exit_dungeon
        

def action(lv,mob,exit_dungeon):
    os.system("cls")
    print("==================================")
    print("Take some action")
    print("1) Healing")
    print("2) Fight")
    print("3) Check inventory")
    print("4) Flee")
    print("==================================")
    
    choice = "0" 
    while choice not in ["1","2","3","4"]:
        choice = input(">> ")
        
        if choice == "1" :
            eating()
        elif choice == "2":
            exit_dungeon = fight(lv,exit_dungeon,mob)
        elif choice == "3":
            steve.display_invt()
        elif choice == "4":
            exit_dungeon = flee(exit_dungeon)
        
    return exit_dungeon

def fight_mobs(lv,exit_dungeon):
    input("Fight mobs")
    name = lvl_info[str(lv)]["mob"]["name"]
    hp = lvl_info[str(lv)]["mob"]["hp"]
    atk = lvl_info[str(lv)]["mob"]["atk"]
    item_drop = lvl_info[str(lv)]["mob"]["item_drop"]

    mob = Mobs(name,hp,atk,item_drop)
    os.system("cls")
    print("============================")
    print()
    print("You encounter",mob.name,"!!!")
    print()
    print("============================")
    input("")
    
    while mob.hp != 0 and (exit_dungeon == False):
        exit_dungeon = action(lv,mob,exit_dungeon)
    
    return exit_dungeon

def found_ore(lv):
    ore = lvl_info[str(lv)]["ore"]
    
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
        
        steve.add_item(ore)
        
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
    


def lv_1(exit_dungeon):
    # ore_chance = 50
    # mob_chance = 50
    
    
    if randint(1,100) <= 50:
        found_ore(1)
    else:
        exit_dungeon = fight_mobs(1,exit_dungeon)
    
    return exit_dungeon
        

def lv_2(exit_dungeon):
    # ore_chance = 30
    # mob_chance = 70
    
    if randint(1,100) <= 30:
        found_ore(2)
    else:
        exit_dungeon = fight_mobs(2,exit_dungeon)
    
    return exit_dungeon

def lv_3(exit_dungeon):
    # ore_chance = 10
    # mob_chance = 90
    
    if randint(1,100) <= 10:
        exit_dungeon = found_ore(3)
    else:
        fight_mobs(3,exit_dungeon)
        
    return exit_dungeon



def next_level(current_level,exit_dungeon):
    
    if current_level == 1:
        exit_dungeon = lv_1(exit_dungeon)
    elif current_level == 2:
        exit_dungeon = lv_2(exit_dungeon)
    elif current_level == 3:
        exit_dungeon = lv_3(exit_dungeon)
    
    return exit_dungeon

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
        #if not
        level += 1            
        exit_dungeon = next_level(level,exit_dungeon)
              
        
        
        
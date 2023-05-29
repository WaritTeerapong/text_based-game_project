from Steve import *

exit_dungeon = False
level = 0

def lv_1():
    pass

def lv_2():
    pass

def lv_3():
    pass

def lv_4():
    pass


def next_level(current_level):
    ore_chance = 0
    mobs_chance = 0
    
    
    
    pass

# main sequence
def dungeon_scene():
    while exit_dungeon == False:
        if level>0:
            print("Would you like to go deeper or back to village")
            print("1) continue exploring")
            print("2) back to village")
            choice = input(">> ")
            
            choice = "0" 
            while choice not in ["1","2"]:
                choice = input(">> ")
                if choice == "1" :
                    
                    break
                elif choice == "2":
                    input("you are exiting dungeon...")
                    exit_dungeon = True
                    
        #exit dungeon
        if exit_dungeon: 
            continue
        level += 1            
        next_level(level)
              
        
        
        
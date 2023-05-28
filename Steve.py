from json import *

# pull item capacity data as item_cap
with open("C:\\Users\\smart\\ProgrammingProjects\\Normal game project\\Mancraft\\Item_Capacity.json", "r") as read_file:
    item_cap = load(read_file)
    
with open("C:\\Users\\smart\\ProgrammingProjects\\Normal game project\\Mancraft\\Item_Ability.json", "r") as read_file:
    item_ablt = load(read_file)
    
#### player setup ####
class player:
    def __init__(self):
        self.hp = 20
        self.invt_cap = 0
        self.invt = []
        
        self.max_invt = 20
    
    #checking inventory
    def check_invt(self):
        return self.invt.sort()   
    
    #add item to vacant inventory
    def add_item(self,new_item):
        while (self.invt_cap + item_cap[new_item] > self.max_invt):
            print("The inventory has not enough space...")
            print("You need to throw something out!")
            print("=== Or do you changed your mind not taking this item ===")
            ans = input("(yes/no) >> ")
            if ans.lower() == "yes":
                return False
            
            self.throw_item()
            
        self.invt.append(new_item)
        self.invt_cap += item_cap[new_item]
        self.invt.sort()
        print(new_item, "has been added.")
        return True
        
    #dump item from inventory
    def throw_item(self):
        if self.invt == []:
            print("Nothing is left in the inventory...")
            return
        
        print("Input the item you want to throw...")
        sad_item = input(">> ")
        
        while (sad_item not in self.invt):
            print("No such item in your inventory...")
            sad_item = input(">> ")
        else:
            self.invt.remove(sad_item)
            self.invt_cap -= item_cap[sad_item] 
            print("You have thrown the", sad_item, "far far away..")
            print("Your inventory capacity :", self.invt_cap)
    
    # health management
    
    def get_damaged(self,damage):
        self.hp -= damage
    
    def healed(self,food):
        if food in item_ablt["heal_item"]:
         self.hp += item_ablt["heal_item"][food]
        else:
            print("You can't get healed from this item")
            
    #display health and inventory capacity
    def display_status(self):
        print("HP:",self.hp,"/ 20")
        print("Bag:",self.invt_cap,"/ 16")
        
    #display inventory
    def display_invt(self):
        print("    _________________    ")
        print("   /    |       |    \\    ")
        print("  |     ---------     |  ")
        print("=========================")
        print("||      Inventory      ||")
        print("||                     ||")
        for i in self.invt:
            print("||",i," "*(len(i)-21),"||")
        print("||                     ||")
        print("=========================")
    
    def has_diamond_pickaxe(self):
        return "diamond pickaxe" in self.inv
    
steve = player()
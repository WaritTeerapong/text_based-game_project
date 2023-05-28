'''text based game :Eng vocab / story'''

import sys 
import os
import time 
import random

from Dungeon_Level import*
from Village import*
from Steve import*



def menu_screen():
    os.system('cls')
    print("===================================")   
    print("|      ?? M A N C R A F T ??      |")   
    print("===================================")
    print("|            - Play -             |")
    print("|            - Exit -             |")
    print("+---------------------------------+")

def menu_selection():
    option = input(">> ")
    if option.lower() == "play":
        introduction()
    elif option.lower() == "exit":
        sys.exit()
    
    # invalid input
    while option not in ["play","exit"]:
        print("I quite not understand. Try again")
        option = input(">> ")
        if option.lower() == "play":
            introduction()
        elif option.lower() == "exit":
            print("Unfortunately, hope we meet again...")
            sys.exit()
        # elif other menu

def introduction():
    # Introduction narated part
    os.system('cls')
    input("Awesome!! Let's get in the world!!")
    os.system('cls')
    input("Welcome to Mancraft!!!")
    os.system('cls')
    input("Well... yeah yeah, it's a Minecraft parody")
    os.system('cls')
    input("Whatever...")
    os.system('cls')
    print("And, you errr... (Enter your name)")
    input(">> ")
    os.system('cls')
    input("Whatever your name is, you are Steve now.")
    os.system('cls')
    input("All you have to do is.... Decide")
    input("Easy right? mate. Decide and Survive, easy like taking programming class.. maybe?")
    os.system('cls')
    input("Then let us Begin~~ ")
    
    

def Prologue():
    os.system('cls')
    # print("First you need to find some resource.")
    # print("You can either find by your self or just wonder around")
    # print("1) Go cut some wood")
    # print("2) Wonder around for a bit")
    

def Prologue_selection():
    choice = int(input("(Input number) >> "))
    if choice == 1:
        Cut_some_wood_scene()
    elif choice == 2 :
        return
    # invalid input
    while choice not in [1,2]:
        print("It's not the choice I expected. Try again?")
        choice = int(input("(Input number) >> "))
        if choice == 1:
            Cut_some_wood_scene()
        elif choice == 2 :
            return
     

def Cut_some_wood_scene():
    print("Steve is cutting some wood",end = "")
    for i in range(3):
        time.sleep(0.5)
        print(".",end="")
    os.system("cls")
    print()
    print("Steve obtain a pile of wood and 3 apple!!")
    input("press any key to continue...")
    
    steve.invt.append("apple")
    steve.invt.append("apple")
    steve.invt.append("apple")
    steve.invt_cap += 3
    
    
    steve.display_status()
    
   
    # game sequence
def start_game():
    menu_screen()
    menu_selection()
    Prologue()
    # Prologue_selection()
    
    while not(steve.has_diamond_pickaxe()) :
        village_scene()
        dungeon_scene()
    
    
start_game()
    
    
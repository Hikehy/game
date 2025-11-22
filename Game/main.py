#Game or whatever idk

#Imports
import os
import json
import random
import platform

#SUPER DUPER IMPORTANT MAIN VARIABLES
userinput = "null"
enemy = None

#loads objects from json
def importjson(file, name):
    with open(file, "r") as f:
        data = json.load(f)
    globals()[name] = data

#clears console on all  platforms
def clearconsole():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


#Creating Objects
importjson("./data/player.json", "player")
importjson("./data/zombie.json", "zombie")
importjson("./data/George.json", "george")
importjson("./data/skeleton.json", "skeleton")

#choose ennemy
def selectenemy():
    global enemy
    data = [zombie, skeleton]
    enemy = random.choice(data)

selectenemy()

def draw():
    print(enemy["name"])
    print(enemy["health"],"\n\n\n\n\n")
    print("Your Health: ", player["health"])
    print("__________________________________________________________________")
    print("1. Attack")
    print("2. Dodge")

#Main funtcion where code goes
def main():
    userinput = input("Option: ")
    match userinput:
        case "0":
            exit(0)
        case "1":
            enemy["health"] -= random.randint(0, player["attack"])
        case _:
            clearconsole()
            print("Not VALID")
            input("")
            draw()
            main()
    enemydodge = random.randint(1, 1000)
    


#Keeps the game running
def gameloop():
    selectenemy()
    while True:
        clearconsole()
        if enemy["health"] < 0 or enemy["health"] == 0:
            print("you win!!!!!")
            exit(0)
        elif player["health"] < 0 or player["health"] == 0:
            print("you died...")
            exit(0)
        elif player["health"] == 67.41:
            print ("THE ONE AND ONLY...")
            print("GEORGE FENTDROID")
        else:
            draw()
            main()
            clearconsole()

gameloop()
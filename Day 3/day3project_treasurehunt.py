## Project - Treasure hunt


# Solution - 


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice == "left":
    river = input("You are at a lake.\n"
                  "There is a island on middle of the lake.\n"
                  "Do you want to swim or wait for boat? swim or wait. \n").lower()
    if river == "wait":
        door = input("You are at the island.\n"
                     "There is a house with three doors.\n"
                     "Which door do you choose? red or yellow or blue. \n").lower()
        if door == "red":
            print("Room is full of fire. \nGame Over.")
        elif door == "yellow":
            print("Found the treasure. You Win!")
        elif door == "blue":
            print("Eaten by beasts. \nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. \nGame Over.")
else:
    print("Game Over.")

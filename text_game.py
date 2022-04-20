"""
The object of this is to make a text based adventure game using functions 
and global variables to represent your character's health. Later on you can 
extend this to make your character a child class of a 'Character' parent class.

As a tip to start off, you can use a function to represent a building, 
and take the building you came from as a parameter.
"""

import time
import random


# ==========EXAMPLE==========

kyle = {"HP": 10, "lives": 3}

def your_house():
    print("You run into your house and slam the door")
    print("You can hear noises outside...")
    
    time.sleep(1)
    print("The monsters are coming! Where do you want to go to?")
    
    time.sleep(0.5)
    print("""
          1 - The church
          2 - The garage down the road
          3 - The abandoned warehouse
          """)
    
    choice = input("Choose a building: ")
    
    # Question - how would you refactor (change) the rest of the code to make this line work?
    # choice = int(input("Choose a building (1, 2 or 3) >> "))
    
    if choice == "church":
        church()
    elif choice == "garage":
        garage()
    elif choice == "warehouse":
        
        print("The monsters come at you and slash your back with huge claws as you run!")
        
        damage = random.randint(1, 7)
        
        print(f"You lose {str(damage)} HP")
        
        kyle['HP'] = kyle['HP'] - damage
        print(f"You now have {kyle['HP']} HP left")
        
        warehouse()
    else:
        print("No, you need to pick one of the above - church, garage or warehouse")
        time.sleep(1)
        your_house()



def church():
    pass

def garage():
    pass

def warehouse():
    pass

your_house()
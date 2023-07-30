print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first = input("You're at a crossroad. Where do you want to go? Type left or right\n").lower()
if first == "left":
    second = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if second == "wait":
        third = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if third == "red":
            print("It's a room full of fire. Game Over.")
        elif third == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

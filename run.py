# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def main_menu():
    """
    Main menu function when the program loads. Allows the user to select New Game,
    Continue and load the previous save state or the help menu for information
    on how to play the game.
    """
    print("Welcome to P-thon, a short Python console-based adventure game.")
    print("Please enter 1 for New Game, 2 to Continue, or 3 for the How to Play.")
    print("If this is your first time, please check the How to Play first. \n")

    while True:
        try:
            choice = int(input("Press the 'Enter' key after making your selection. \n"))
            
            if choice == 1:
                first_room()
                break
            elif choice == 2:
                continue_game()
                break
            elif choice == 3:
                how_to_play()
                break
            else:
                raise ValueError (
                    f"{choice} is not a valid option. Please try again. \n"
                )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-3).\n")
            else:
                print(e)

def continue_game():
    """
    Function prompts User to enter a code. If user enters code correctly, function loads
    the correct room and inventory in the inventory dictionary that the User had at that time.
    """
    print("Continue Game")

def how_to_play():
    """
    Set of instruction paragraphs on how to play P-thon. User must select Enter key to 
    end function and move back to main_menu().
    """
    print("P-thon is a text-based mini-adventure played entirely in the console. \n")
    input("Press Enter to continue... \n")
    print("You will need to type numbers when prompted to make decisions ")
    print("and some progress will be locked if you do not try everything. \n")
    input("Press Enter to continue... \n")
    print("When you enter a room, you will be given a code. Write this code down!")
    print("It is a save state that monitors the room you just entered and your current")
    print("inventory.")
    input("Press Enter to continue... \n")
    print("If you forget your code, or do not write it down,")
    print("you will need to start from the beginning. \n")
    input("Press Enter to continue... \n")
    print("Have fun! When you are ready, press 'Enter' to go back to the Main Menu.")
    input("Press Enter to continue... \n")
    main_menu()

def first_room():
    """
    First room function, introduces user to Move and Look options. Move progresses
    to second_room() whilst Look activates first_room_look(). User can use Move without
    the Look function.
    """

    print("Creating save code... \n")
    print(f"Your code is: ")

    print("....... \n")
    print("You gain consciousness without warning and find yourself in a stone room. \n")
    input("Press Enter to continue... \n")
    print("The walls are polished grey brick, neatly arranged on all sides, the ceiling,")
    print("and the floor with torches evenly spaced to illuminate the room comfortably. \n")
    input("Press Enter to continue... \n")
    print("As you look at your hands, you notice that they are white and knobbly,")
    print("and you feel as if they are naked somehow. Your legs and chest are the same.")
    print("You also cannot talk, or feel... or breathe... But you are alive. \n")
    input("Press Enter to continue... \n")
    print("You decide not to dwell on this and instead look for a way out.")
    print("There is a door at the far end of the room, but there may also be")
    print("something else here if you search for it. \n")
    input("Press Enter to continue... \n")
    print("1: Move through the door.")
    print("2: Look around the room.")

    while True:
        try:
            choice = int(input("Press the 'Enter' key after making your selection. \n"))
            
            if choice == 1:
                second_room()
                break
            elif choice == 2:
                first_room_look()
                break            
            else:
                raise ValueError (
                    f"{choice} is not a valid option. Please try again. \n"
                )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-2).\n")
            else:
                print(e)


def first_room_look():
    '''
    Provides user with sword which is written to the user's inventory. The moves user
    automatically to second_room().
    '''
    print("You decide to look around the room for anything you can use,")
    print("you are uncertain what lies ahead of that door after all. \n")
    input("Press Enter to continue... \n")
    print("There are a number of piles of books and papers strewn about,")
    print("some mostly empty shelves, a table, a chair, and a skull. \n")
    input("Press Enter to continue... \n")
    print("After rummaging through the books for a bit too long, you notice")
    print("something sparkle from the corner of your eye socket - a sword. \n")
    input("Press Enter to continue... \n")
    print("You pick up the sword in your dominant hand and, feeling a bit more")
    print("prepared, head to the next room. \n")
    input("Press Enter to continue... \n")

    inventory["sword"] = True

    second_room()

def second_room():
    '''
    Similar to first_room(), providing Move and Look options. Initiates first combat
    sequence with options to Fight or Defend when Move option selected. If user defends, they fail. 
    If they attack without a sword, they fail. If they attack with a sword, they succeed.
    '''
    print("Movin' on? Potentially a mistake")

def second_room_look():
    '''
    Provides user with shield item, written into user's inventory. Provides Move and Look Again
    options. 
    '''

    inventory["shield"] = True

def second_room_second_look():
    '''
    Provides context to User that they find nothing but that there might be something more. Provides
    Move and Look Once More option. Look Once More option moves on to secret_room().
    '''

def secret_room():
    """
    Automatic function that informs the User of a secret room that was found. 
    A secret_room_item is added to the User's inventory and then immediately activates final_room().
    """
    print("You walk through a dimly lit tunnel for what seems to be over an hour. \n")
    input("Press Enter to continue... \n")
    print("The only sounds are your own footsteps and the gentle crackling of each torch")
    print("as you pass them by. \n")
    input("Press Enter to continue... \n")
    print("Finally you see a light in the distance, and quicken your step to reach what you")
    print("hope is an exit. \n")
    input("Press Enter to continue... \n")
    print("To your immeasurable disappointment, it is in fact another dungeon room, simlar to")
    print("the others, with two distinct differences that pique your curiosity: \n")
    input("Press Enter to continue... \n")
    print("The first is a chest in the centre of the room. The second is a purple portal behind it. \n")
    input("Press Enter to continue... \n")
    print("You walk to the chest and carefully lift the lid, ready for another ambush...")
    print("But nothing happens. You peek inside and find a strange handheld device. \n")
    input("Press Enter to continue... \n")
    print("It is mostly metallic, with a wooden handle and a strange engraving you cannot deciper.")
    print("There is a hole at the long end and some kind of trigger underneath that your index")
    print("finger can gently rest in. It is comfortable to hold and not particularly heavy")
    print("with the number 7 scratched into the side. \n")
    input("Press Enter to continue... \n")
    print("You deduce that this is a weapon and can be used a total of 7 times.")
    print("New weapon in hand, you step through the portal, ready for what comes next... \n")
    input("Press Enter to continue... \n")

    inventory["secret_item"] = True

    final_room()

def final_room():
    '''
    Function that initiates an automatic fight after lore pre-amble. 
    Should User have sword and shield, they will need to Defend first, then Attack to succeed.
    Should User have secret_room_item they will get the option to use it, immediately succeeding the fight.
    Upon succeeding, credits roll and main_menu() is loaded.
    '''
    if inventory["secret_item"] == True:
        print("Oh shit, he's got a gun!")
    else:
        print("So... You've finally come...")

inventory = {
    "sword": False,
    "shield": False,
    "secret_item": False
}

main_menu()
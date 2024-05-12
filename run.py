# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

class colours:
    RED = '\033[31m'
    GREEN = '\033[32m'
    ENDC = '\033[m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'

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
            choice = int(input(colours.GREEN + "Press the 'Enter' key after making your selection.  \n" + colours.ENDC))
            
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
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You will need to type numbers when prompted to make decisions ")
    print("and some progress will be locked if you do not try everything. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("When you enter a room, you will be given a code. Write this code down!")
    print("It is a save state that monitors the room you just entered and your current")
    print("inventory.")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("If you forget your code, or do not write it down,")
    print("you will need to start from the beginning. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Have fun! When you are ready, press 'Enter' to go back to the Main Menu.")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    main_menu()


def choice(text, func1, func2):
    """
    Repeating function to allow User to make a choice of either 1 or 2.
    """
    while True:
        try:
            choice = int(input(text))
            
            if choice == 1:
                func1()
                break
            elif choice == 2:
                func2()
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
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The walls are polished grey brick, neatly arranged on all sides, the ceiling,")
    print("and the floor with torches evenly spaced to illuminate the room comfortably. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("As you look at your hands, you notice that they are white and knobbly,")
    print("and you feel as if they are naked somehow. Your legs and chest are the same.")
    print("You also cannot talk, or feel... or breathe... But you are alive. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You decide not to dwell on this and instead look for a way out.")
    print("There is a door at the far end of the room, but there may also be")
    print("something else here if you search for it. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("1: Move through the door.")
    print("2: Look around the room.")

    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, second_room, first_room_look)


def first_room_look():
    '''
    Provides user with sword which is written to the user's inventory. The moves user
    automatically to second_room().
    '''
    print("You decide to look around the room for anything you can use,")
    print("you are uncertain what lies ahead of that door after all. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("There are a number of piles of books and papers strewn about,")
    print("some mostly empty shelves, a table, a chair, and a skull. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("After rummaging through the books for a bit too long, you notice")
    print("something sparkle from the corner of your eye socket - a sword. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You pick up the sword in your dominant hand and, feeling a bit more")
    print("prepared, head to the next room. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    inventory["sword"] = True
    print(colours.BLUE + "Sword obtained! \n" + colours.ENDC)
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    second_room()

def second_room():
    '''
    Similar to first_room(), providing Move and Look options. Initiates first combat
    sequence with options to Fight or Defend when Move option selected. If user defends, they fail. 
    If they attack without a sword, they fail. If they attack with a sword, they succeed.
    '''
    print("As you walk through the corridor to the next room, you have a thought:")
    print("You are a skeleton. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You are not sure how, or why, but you are a reanimated skeleton.")
    print("No memories, no voice, no skin... No way to live, in your opinion.")
    print("Maybe if you find who did this, you can undo it, or get skin at least. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Your thoughts are then interrupted by the skittering of small feet,")
    print("a fiendish growl, and a club in a green hand. A goblin attacks! \n")
    print("What do you do?")
    print("1: Attack")
    print("2: Defend \n")

    while True:
        try:
            fight_choice = int(input(colours.GREEN + "What do you do? \n" + colours.ENDC))
            if fight_choice == 1 and inventory["sword"] == False:
                print("You instinctively strike first at the goblin with your bare fist.")
                print("However, being made of bone and with no muscles or tendons,")
                print("your hand and wrist fall apart on impact. \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The goblin snickers and swings its club into your head.")
                print("You fall apart and slowly drift out of conciousness... \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("GAME OVER. \n")
                print("Maybe you can find something to defend yourself with? \n")
                input(colours.GREEN + "Press Enter to return to the Main Menu... \n" + colours.ENDC)
                main_menu()
                break
            elif fight_choice == 2:
                print("You instinctively bring your arms to your face in an attempt to")
                print("protect yourself. However...")
                input(colours.GREEN + "Press Enter to continue..." + colours.ENDC)
                print("The goblin strikes your arms with his club, shattering them and")
                print("connecting with your skull. As your head hits the floor, you watch")
                print("as the goblin pushes your body over and begins gnawing on your thigh.")
                input(colours.GREEN + "Press Enter to continue..." + colours.ENDC)
                print("Your mind fades. At least the goblin will not go hungry for a while... \n")
                print("GAME OVER. \n")
                print("Offense may be the best defence against this opponent. \n")
                input(colours.GREEN + "Press Enter to return to the Main Menu..." + colours.ENDC)
                main_menu()
                break
            elif fight_choice == 1 and inventory["sword"] == True:
                print("You instinctively thrust your sword at the goblin who, taken by surprise,")
                print("does not react until your blade pierces clean through its chest. \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The goblin looks at you mouth agape and begins to move its arm towards you.")
                print("You pull the sword out from its chest and watch as it hits the floor.")
                print("The goblin is motionless, green blood beginning to pool underneath it.")
                print("You almost feel sorry for it... \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
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

    print("With the encounter over, you calm the shaking in your arms and prepare your")
    print("next course of action. \n")
    input(colours.GREEN + "Press Enter to continue \n" + colours.ENDC)
    print("As before you see a doorway infront of you")
    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, final_room, second_room_look)

def second_room_look():
    '''
    Provides user with shield item, written into user's inventory. Provides Move and Look Again
    options. 
    '''

    print("You feel off about looking through this goblin's room, especially")
    print("with the corpse still there, but you may need something else to")
    print("help you with the remainder of your journey. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("After some respectful rummaging, you find a metal kite shield embellished")
    print("with a symbol of a cockatiel for some reason. You decide to take it. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    inventory["shield"] = True
    print(colours.BLUE + "Shield obtained! \n" + colours.ENDC)
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    print("Shield in your off-hand, you feel ready to continue... Except for an uneasiness")
    print("as if there is something else here...")
    print("What will you do?")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("1. Move to the Final Room")
    print("2. Look around again")

    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, final_room, second_room_second_look)

def second_room_second_look():
    '''
    Provides context to User that they find something in the wall.
    Moves on to secret_room().
    '''
    print("This time around you searched the walls themselves. You noticed that")
    print("some of the bricks were slightly off colour compared to the rest.")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("After touching and prodding and pushing, you move the wall itself to the side")
    print("revealing a hidden passage. Perhaps it leads outside, or to whatever did this")
    print("to you! Only one way to find out...")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    secret_room()

def secret_room():
    """
    Automatic function that informs the User of a secret room that was found. 
    A secret_room_item is added to the User's inventory and then immediately activates final_room().
    """
    print("You walk through a dimly lit tunnel for what seems to be over an hour. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The only sounds are your own footsteps and the gentle crackling of each torch")
    print("as you pass them by. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Finally you see a light in the distance, and quicken your step to reach what you")
    print("hope is an exit. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("To your immeasurable disappointment, it is in fact another dungeon room, simlar to")
    print("the others, with two distinct differences that pique your curiosity: \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The first is a chest in the centre of the room. The second is a purple portal behind it. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You walk to the chest and carefully lift the lid, ready for another ambush...")
    print("But nothing happens. You peek inside and find a strange handheld device. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("It is mostly metallic, with a wooden handle and a strange engraving you cannot deciper.")
    print("There is a hole at the long end and some kind of trigger underneath that your index")
    print("finger can gently rest in. It is comfortable to hold and not particularly heavy")
    print("with the number 7 scratched into the side. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You deduce that this is a weapon and can be used a total of 7 times.")
    print("New weapon in hand, you step through the portal, ready for what comes next... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    inventory["secret_item"] = True
    print(colour.BLUE + "Secret Weapon obtained! \n" + colours.ENDC)

    final_room()

def final_room():
    '''
    Function that initiates an automatic fight after lore pre-amble. 
    Should User have sword and shield, they will need to Defend first, then Attack to succeed.
    Should User have secret_room_item they will get the option to use it, immediately succeeding the fight.
    Upon succeeding, credits roll and main_menu() is loaded.
    '''

    print("You finally reach the final room on of this admittedly small dungeon. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The walls are an obsidian black, bright red sconces peppering the walls,")
    print("and at the back of the room in front of an ornate door, a robed figure stands. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You feel nervous; your bones shaking as you stare at the hooded spectre.")
    print("Steeling yourself, take a step towards the entity... And they speak... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print('"Ah! There you are, at last, Skelley-lad!" \n')
    print("You stare dumbfounded at the now un-hooded old man in front of you.")
    print("He seems ancient; valley-like wrinkles cover his face, three teeth")
    print("make up his smile, and you are unsure, but you think he is also blind. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("As he walks towards you, he bumps into a table. Definitely blind.")
    print('"Oh, blasted thing. I swore I moved that aside. Now, Skelly-lad." \n')
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("If you could roll your eyes at the name, you would.")
    print('"You are dead. If you didnt guess already, but I brought you back!"')
    print('"Got rid of all that pesky skin for ya too. I will take my thanks now." \n')
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The only thought racing through your mind is that he did this to you.")
    print("If he brought you back, then taking him out will end your suffering.")
    print("You ready your stance, and the Old Necromancer notices the shift.")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print('"Oh, so thats how you want to play? Fine."')
    print("The air pressure, the mood, your calm - it all changes in an instant.")
    print("The Old Man is preparing to fight you with everything he has.")
    print("What will you do?")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("1: Fight")
    print("2: Surrender")

    if inventory["secret_item"] == True:
        print("Oh shit, he's got a gun!")
    else:
        print("So... You've finally come...")


def credits():
    """
    Function that tells the end of the story if the User is successful in final_room().
    Recalls the main_menu() when done.
    """

    print("The end. Thank you for playing!")
    input(colours.GREEN + "Press Enter to return to the Main Menu. \n" + colours.ENDC)
    main_menu()

inventory = {
    "sword": False,
    "shield": False,
    "secret_item": False
}

main_menu()
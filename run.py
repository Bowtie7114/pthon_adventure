import re


class colours:
    RED = '\033[31m'
    GREEN = '\033[32m'
    ENDC = '\033[m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'


def save_codes(room):
    """
    Function that generates a save code based on which room the User is in
    and the state of the inventory by assigning a code to each room reading
    said code as the beginning of each room function load and combining it
    with the state of the dictionary at that time.
    Then displays combined code to the user.
    """

    save_code = room
    if inventory["sword"]:
        save_code += "s1"
    else:
        save_code += "s0"
    if inventory["shield"]:
        save_code += "sh1"
    else:
        save_code += "sh0"
    if inventory["secret_item"]:
        save_code += "si1"
    else:
        save_code += "si0"
    print(colours.YELLOW + f"Your save code is: {save_code} \n" + colours.ENDC)


def main_menu():
    """
    Main menu function when the program loads. Allows user to select New Game,
    Continue the previous save state or the help menu for information
    on how to play the game.
    """
    print("Welcome to P-thon, a short Python console-based adventure game.")
    print("Please enter 1: for New Game")
    print("2: for Continue")
    print("3: for How to Play. \n")
    print("If this is your first time, please check the How to Play first. \n")

    while True:
        try:
            choice = int(input(colours.GREEN + "Press the 'Enter' after making your selection.  \n" + colours.ENDC))
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
                raise ValueError(
                    f"{choice} is not a valid option. Please try again. \n"
                )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-3).\n")
            else:
                print(e)


def continue_game():
    """
    Function prompts User to enter a code.
    If user enters code correctly, function loads
    the correct room and inventory in the inventory
    dictionary that the User had at that time.
    """
    code = input(colours.GREEN + "Please enter your code and press Enter... \nTo return to Main Menu, type exit and press Enter... \n" + colours.ENDC)

    check_code = re.compile("^00[0-3]s[0,1]sh[0,1]si[0,1]$")
    if code == "exit":
        main_menu()
    if not check_code.match(code):
        print("This code is not valid. Please enter a valid code. \n")
        continue_game()

    if code[4] == "1":
        inventory["sword"] = True
    if code[7] == "1":
        inventory["shield"] = True
    if code[10] == "1":
        inventory["secret_item"] = True
    if code[0:3] == "001":
        first_room()
    if code[0:3] == "002":
        second_room()
    if code[0:3] == "003":
        final_room()


def how_to_play():
    """
    Set of instruction paragraphs on how to play P-thon.
    User must select Enter key to
    end function and move back to main_menu().
    """
    print("P-thon is a text-based mini-adventure played entirely in the console. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You will need to type numbers when prompted to make decisions ")
    print("and some progress will be locked if you do not try everything. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("When you enter a room, you will be given a code. Write this code down!")
    print("It is a save state that monitors the room you just entered and your current")
    print("inventory. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("If you forget your code, or do not write it down,")
    print("you will need to start from the beginning. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("If you need to restart the game, press the Run Program button above. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Have fun! \n")
    input(colours.GREEN + "Press Enter to return to the Main Menu... \n" + colours.ENDC)
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
                raise ValueError(
                    f"{choice} is not a valid option. Please try again. \n"
                )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-2).\n")
            else:
                print(e)


def first_room():
    """
    First room function, introduces user to Move and Look options.
    Move progresses to second_room() whilst Look activates
    first_room_look(). User can use Move without
    the Look function.
    """

    save_codes("001")

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
    Provides user with sword which is written to the
    user's inventory. The moves user
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
    Similar to first_room(), providing Move and Look options.
    Initiates first combat sequence with options to Fight or Defend
    when Move option selected. If user defends, they fail.
    If they attack without a sword, they fail.
    If they attack with a sword, they succeed.
    '''

    save_codes("002")

    print("....... \n")
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
            if fight_choice == 1 and inventory["sword"] is False:
                print("You instinctively strike first at the goblin with your bare fist.")
                print("However, being made of bone and with no muscles or tendons,")
                print("your hand and wrist fall apart on impact. \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The goblin snickers and swings its club into your head.")
                print("You fall apart and slowly drift out of conciousness... \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print(colours.RED + "GAME OVER. \n" + colours.ENDC)
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
                print(colours.RED + "GAME OVER. \n" + colours.ENDC)
                print("Offense may be the best defence against this opponent. \n")
                input(colours.GREEN + "Press Enter to return to the Main Menu..." + colours.ENDC)
                main_menu()
                break
            elif fight_choice == 1 and inventory["sword"] is True:
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
                raise ValueError(
                    f"{choice} is not a valid option. Please try again. \n"
                )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-2).\n")
            else:
                print(e)

    print("With the encounter over, you calm the shaking in your arms and prepare your")
    print("next course of action. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("As before you see a doorway infront of you, but it may be prudent to search")
    print("your surroundings before carrying on. What will you do? \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("1: Move on")
    print("2: Look around \n")
    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, final_room, second_room_look)


def second_room_look():
    '''
    Provides user with shield item.
    Provides Move and Look Again options.
    '''

    print("You feel off looking through this goblin's room, especially")
    print("with the corpse still there, but you may find something else to")
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
    print("2. Look around again \n")

    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, final_room, second_room_second_look)


def second_room_second_look():
    '''
    Provides context to User that they find something in the wall.
    Moves on to secret_room().
    '''
    print("This time around you searched the walls themselves. You noticed that")
    print("some of the bricks were slightly off colour compared to the rest. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("After touching and prodding and pushing, you move the wall itself to the side")
    print("revealing a hidden passage. Perhaps it leads outside, or to whatever did this")
    print("to you! Only one way to find out... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    secret_room()


def secret_room():
    """
    Automatic function that informs the User of a secret room that was found.
    A secret_room_item is added to the User's inventory and then
    immediately activates final_room().
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
    print("New weapon tucked in a conveniently shaped slot in the back of your shield,")
    print("you step through the portal, ready for what comes next... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    inventory["secret_item"] = True
    print(colours.BLUE + "Secret Weapon obtained! \n" + colours.ENDC)
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)

    final_room()


def final_room():
    '''
    Function that gives the User the choice of a fight after lore pre-amble.
    If User decides to Surrender, lore rolls and the game ends.
    Should User have sword and shield, they will need to Defend first,
    then Attack to succeed. Should User have secret_room_item they will
    get the option to use it, immediately succeeding the fight.
    Upon succeeding, credits roll and main_menu() is loaded.
    '''

    save_codes("003")

    print("....... \n")
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
    print('"Got rid of all that pesky skin for ya too, makes it much easier to do')
    print('chores when you dont get tired or bruised! Thank me anytime, by the way." \n')
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The only thought racing through your mind is that he did this to you.")
    print("If he brought you back, then taking him out will end your suffering.")
    print("You ready your stance, and the Old Necromancer notices the shift. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print('"Oh, so thats how you want to play? Fine."')
    print("The air pressure, the mood, your calm - it all changes in an instant.")
    print("The Old Man is preparing to fight you with everything he has. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("What will you do? \n")
    print("1: Fight")
    print("2: Surrender \n")

    choice(colours.GREEN + "Press the 'Enter' key after making your selection. \n" + colours.ENDC, final_fight, surrender)


def final_fight():
    """
    If the User does not have the secret_item, plays the fight scene
    as normal with the sword and shield. If they do have the secret_item
    it gives them the choice to use that or the sword and shield.
    """
    print("Despite your shaking bones and an overwhelming sense of dread,")
    print("you stand firm, weapons at the ready - do or die... Again! \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print('"I hope you are ready, Skelly-boy! Here comes some magic!" \n')

    while True:
        if inventory["secret_item"] is True:
            try:
                print("Choose how to fight: \n")
                print("1: Sword and Shield")
                print("2: Secret Weapon \n")
                weapon_choice = int(input(colours.GREEN + "Press Enter after making your choice... \n" + colours.ENDC))
                if weapon_choice == 1:
                    break
                elif weapon_choice == 2:
                    print("You drop the sword out of your dominant hand and unsheath the weapon")
                    print("you found in the secret passage. Pointing it at the wizard, you know")
                    print("not what it will do, only that it will be effective. \n")
                    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                    print("The wizard suddenly stops and blurts out:")
                    print('"Wait... Is that a gun?? Where the hell did you even get that??" \n')
                    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                    print("Sensing the wizard's fear, you aim and pull the trigger. \n")
                    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                    print("A loud crack fills the air and the wizard drops to the ground.")
                    print("You are not sure what this 'gun' is, but it certainly worked. \n")
                    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                    credits()
                    break
                else:
                    raise ValueError(
                        f"{choice} is not a valid option. Please try again. \n"
                    )
            except ValueError as e:
                if "literal" in str(e):
                    print(f"Invalid data: {e}, please use a number (1-2).\n")
                else:
                    print(e)
        else:
            break

    print("The wizard waves his hands in an intricate pattern before fire begins")
    print("to erupt from his fingertips. An attack is coming, you need to act. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("What do you do? \n")
    print("1: Attack")
    print("2: Defend \n")

    while True:
        try:
            battle_choice = int(input(colours.GREEN + "Press Enter after making your choice... \n" + colours.ENDC))
            if battle_choice == 1:
                print("You charge in for an attack and swing your sword horizontally, hoping")
                print("to strike the wizard's chest. However, the wizard fires a volley of")
                print("fireballs before your blow connects. \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The fireballs hit your ribs, arms, legs - everwhere, each shattering")
                print("upon the incredible force of the spells.\n")
                print("The world goes black before you know it...\n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print(colours.RED + "GAME OVER \n" + colours.ENDC)
                input(colours.GREEN + "Press Enter to return to the Main Menu... \n" + colours.ENDC)
                main_menu()
            elif battle_choice == 2:
                break
            else:
                raise ValueError(
                    f"{choice} is not a valid option. Please try again. \n"
                    )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-2).\n")
            else:
                print(e)

    print("Predicting the incoming attack, you raise your shield and stand your ground.")
    print("A large fireball manifests in the air above the Old Man who waves his hand")
    print("towards you, hurtling the fireball at you. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You duck your skull behind the shield and brace as a massive impact rocks")
    print("you to the core, a blinding flash of light accompanying the tremors. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Though your head is still covered by the shield, you hear the wizard")
    print("panting - that must have taken a lot out of him. What will you do now? \n")
    print("1: Attack")
    print("2: Defend \n")

    while True:
        try:
            battle_choice2 = int(input(colours.GREEN + "Press Enter after making your choice... \n" + colours.ENDC))
            if battle_choice2 == 1:
                print("Sensing your opportunity, you quickly lower your shield and charge the old man,")
                print("swinging your sword across the chest, making a deep cut into the wizard. \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The wizard stumbles backwards, unable to catch his breath. You stay at the")
                print("ready just in case but notice that, just as the wizard falls to the ground,")
                print("he seems to smile ever so slightly at you...")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The Old Man hits the ground with a thump... \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                credits()
            elif battle_choice2 == 2:
                print("Not taking any chances, you stay hidden beneath your shield for a moment...")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("As you notice your head suddenly moving without your body, you realise")
                print("that may have been a mistake. The wizard removed your head from your")
                print("shoulders when you weren't looking! \n")
                input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
                print("The wizard proceeds to lecture you on being grateful, going on long")
                print("tangents about his youth, the perfect blueberry pie, and some very")
                print("unsavoury things about warlocks... \n")
                print(colours.RED + "GAME OVER \n" + colours.ENDC)
                input(colours.GREEN + "Press Enter to return to the Main Menu... \n" + colours.ENDC)
                main_menu()
            else:
                raise ValueError(
                    f"{choice} is not a valid option. Please try again. \n"
                    )
        except ValueError as e:
            if "literal" in str(e):
                print(f"Invalid data: {e}, please use a number (1-2).\n")
            else:
                print(e)


def surrender():
    """
    User surrenders fight, is given story content, then the main_menu loads.
    """
    print("As the air around you swirls and rage, light appearing from random corners")
    print("of the dim room, you are unable to act, to move, to even think. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("In a moment of terror filled clarity you drop everything and fall")
    print("to your knees with a clatter, throwing up your arms. You surrender.")
    print("The old wizard realises that you have lost the will to fight and speaks: \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print('"Well, you had me worried there, Skelly-Boy! Be a shame to kill you again."')
    print("Again? So he killed you before? Was he the reason for EVERYTHING?")
    print('"Stay still now, dont want to mess this up again. Mind control is tricky!" \n')
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("He chuckles and begins casting a spell on you. Your mind starts to go blank.")
    print("The last thing you remember before it all goes black is the old man:")
    print('"I hope you can cook well, I happen to be a picky eater!" \n')
    print(colours.RED + "GAME OVER \n" + colours.ENDC)
    input(colours.GREEN + "Press Enter to return to the Main Menu... \n" + colours.ENDC)
    main_menu()


def credits():
    """
    Function that tells the end of the story if the User
    is successful in final_room(). Recalls main_menu() when done.
    """
    print("You drop your armaments to the floor and take it all in.")
    print("How long have you been here? A few hours? Days? A lot happened in that time.")
    print("But now the door to freedom lies in front of you, and you plan to take it. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("You take one step forward and immediately fall to the ground, your bones")
    print("scattering across the floor... Looks like killing the old man undid")
    print("the spell keeping alive after all. \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("But, this is fine. You have accepted this and welcome it. Living as a")
    print("skeleton is no way to live, after all. You let yourself slowly fade, at")
    print("peace that you can rest... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("... \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("Did you hear a sound?...")
    print('"...can....... -tle more..."')
    print("Voices? From where? You can no longer see, so who..? \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("This sensation, you have felt it before. Warmth, touch... Light!")
    print('"Nearly there, one more big push!"')
    print("The voices are so clear now... What is happening? \n")
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("All these sensations are too much... You are so tired.")
    print("Before you fall asleep, you hear one final phrase:")
    print('"Congratulations! Your baby is healthy and whole..." \n')
    input(colours.GREEN + "Press Enter to continue... \n" + colours.ENDC)
    print("The end. Thank you for playing! \n")
    input(colours.GREEN + "Press Enter to return to the Main Menu. \n" + colours.ENDC)
    main_menu()


inventory = {
    "sword": False,
    "shield": False,
    "secret_item": False
}


main_menu()

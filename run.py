# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def main_menu():
    """
    Main menu function when the program loads. Allows the user to select New Game,
    Continue and load the previous save file, or the help menu for information
    on how to play the game.
    """
    print("Welcome to P-thon, a short Python console-based adventure game. \n")
    print("Please enter 1 for New Game, 2 to Continue, or 3 for the How to Play. \n")
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
                print(f"Invalid data: {e}, please use a number.\n")
            else:
                print(e)

def continue_game():
    """
    Functions looks through downloads folder of User PC for save file. If once does not
    exist, flags error and re-directs to main_menu(). If it does, read room function saved
    and appropriate function.
    """
    print("Continue Game")

def how_to_play():
    """
    Set of instruction paragraphs on how to play P-thon. User must select Enter key to 
    end function and move back to main_menu().
    """
    print("How to Play")

def first_room():
    """
    First room function, introduces user to Move and Look options. Move progresses
    to second_room() whilst Look activates first_room_look(). User can use Move without
    the Look function.
    """
    print("Lol can has cheeseburger")

def first_room_look():
    '''
    Provides user with sword which is written to the user's inventory. The moves user
    automatically to second_room().
    '''

def second_room():
    '''
    Similar to first_room(), providing Move and Look options. Initiates first combat
    sequence with options to Fight or Defend when Move option selected. If user defends, they fail. 
    If they attack without a sword, they fail. If they attack with a sword, they succeed.
    '''

def second_room_look():
    '''
    Provides user with shield item, written into user's inventory. Provides Move and Look Again
    options. 
    '''

def second_room_second_look():
    '''
    Provides context to User that they find nothing but that there might be something more. Provides
    Move and Look Once More option. Look Once More option moves on to secret_room().
    '''

def secret_room():
    '''
    Automatic function that informs the User of a secret room that was found. 
    A secret_room_item is added to the User's inventory and then immediately activates final_room().
    '''

def final_room():
    '''
    Function that initiates an automatic fight after lore pre-amble. 
    Should User have sword and shield, they will need to Defend first, then Attack to succeed.
    Should User have secret_room_item they will get the option to use it, immediately succeeding the fight.
    Upon succeeding, credits roll and main_menu() is loaded.
    '''

main_menu()
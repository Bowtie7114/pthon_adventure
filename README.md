## Table Of Contents

* [Introduction](#Introduction)
    * [Site Goals](#Site-Goals)
    * [Target Audience](#Target-Audience)
    * [User stories](#User-Stories)
    * [Features Planned](#Features-Planned)
* [Structure](#Structure)
    * [Features](#Features)
    * [Features left to Implement](#Features-Left-to-Implement)
* [Logical Flow](#Logical-Flow)
* [Database Design](#Database-Design)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Functional Testing](#Functional-Testing)
    * [Pep8 Validation](#Pep8-Validation)
    * [Bugs and Fixes](#Bugs-and-Fixes)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [MongoDB Setup](#MongoDB-Setup)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Clone Locally](Clone-Locally)
* [Credits](#Credits)
  * [Content](#Content)


## Introduction


## Structure

## Logical Flow
Main Menu:<br>
![Flowchart Main Menu](docs/readme_images/flow_main_menu.PNG)<br><br>

First Room:<br>
![Flowchart First Room](docs/readme_images/flow_first_room.PNG)<br><br>

Second Room:<br>
![Flowchart Second Room](docs/readme_images/flow_second_room.PNG)<br><br>

Secret Room:<br>
![Flowchart Secret Room](docs/readme_images/flow_secret_room.PNG)<br><br>

Final Room:<br>
![Flowchart Final Room](docs/readme_images/flow_final_room.PNG)<br><br>

## Database Design

## Technologies
- Python:
    Used as the primary programming language for the entire project, except the pre-defined packages.
- Gitpod:
    Used as the IDE to write, test, and modify the programme.
- Github:
    Used as the repository to store the code and README.
- Heroku:
    Used as the hosting platform, allowing Users to activate the program in their web browser.

## Testing

- Upon testing the ability to create a save file for the User, I discovered that the file saved to the directory when not given a path to follow. This was set to the Downloads folder
for the User, however I then learned that this would not work as the IDE and Heroku host both utilise a web browser, which did not give access to the User's files. As such, the
Save File system was removed for a Dictionary for the Inventory system and a Code-based Save System; the User is given a code based on the room they were last in and the items they had
at that time which, when given at the continue_game function, loads the appropriate room/dictionary values.

### Bugs

- When selecting a path on the main_menu() function, the test print ran as expected and then the User was prompted to enter an input value again, initiating an infinite loop.
Adding a break after each option removed the infinite loop.
- When testing the first fight scene, received error code: function choice at 0x7f20da532020. I had forgotten to change the fight_choice input to an int(). Changing this allowed the code to function, but then 
revealed another bug;
- Within the if statement for fight_choice in second_room(), the first if fight_choice == 1 statement ended there. As such, whether or not the sword was present in the inventory, it would always run the first option.
Changed the code to if fight_choice == 1 and inventory[sword] == False to rectify.

## Deployment

## Credits
- Code institute for providing the pre-installed code to run the code via browser-based terminal.
- Fiancé [Magdalena]() for assistance with Python syntax (if "literal" in str(e): in main_menu())
- Fiancé [Magdalena]() for the idea of using RegEx to check if save code was entered correctly.
- File write function help from [Free Code Camp](https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/).
- [Geeks for Geeks](https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/) with refresher on function arguments.
- [W3Schools](https://www.w3schools.com/python/default.asp) for various python reminders.
- [W3Schools](https://www.w3schools.com/python/python_regex.asp) for information on how to check string using RegEx.
- User Kevin Chou on [Stack Overflow](https://stackoverflow.com/questions/37340049/how-do-i-print-colored-output-to-the-terminal-in-python) for the information on setting colour console text.
- [Regex101](https://regex101.com/) as a RegEx syntax checking site to ensure what I used worked correctly.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

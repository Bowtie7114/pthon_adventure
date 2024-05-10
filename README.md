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
### Bugs

- When selecting a path on the main_menu() function, the test print ran as expected and then the User was prompted to enter an input value again, initiating an infinite loop.
Adding a break after each option removed the infinite loop.

## Deployment

## Credits
- Code institute for providing the pre-installed code to run the code via browser-based terminal.
- Fiancé [Magdalena]() for assistance with Python syntax (if "literal" in str(e): in main_menu())


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

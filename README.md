# Cyberpunk - A text based RPG

## Requirements:
- There are no special requirements needed for this application. Only the random import is used.

## Introduction:
This cyberpunk roleplaying game is based on the tabletop game Cyberpunk 2020 and also a small reference to the game Cyberpunk 2077.
To stay true to an MVP, this text-based game offers some strategic options without becoming too complex. At the start, the player can choose a life path from two options.
Hacker: In this life path, one has an attempt to crack a secret PIN. With the right PIN, the game is won immediately. With the wrong PIN, the player is caught by security and loses 50% life energy in a battle against a Cyber-Thug.
The player can also choose the life path of an adventure.
In this case, the player fights against the computer (Cyber Thug).
The player can choose to "fight" or "talk" in the battle.
Each hit by "fight" causes damage to the life energy. Life energy of 0 will mean losing the game.
The decision for "talk", i.e. the attempt of a negotiation to de-escalate the situation, increases two values: humanity and empathy.
When the values of humanity and empathy reach a maximum value of 100 each, the respective party has won.
The decision to fight, however, causes the values for humanity and empathy to decrease. If both values reach 0, the fight is lost for the respective party.
This principle allows for some strategic considerations. A battle can be lost through fighting, just as a battle can be won through negotiation.

## Features:

### Game Features:
To keep the readme more concise, you can find the screenshots in the "How to Play" and "Testing" section.

- Cyberpunk-themed ASCII banner
- Text-based RPG elements
- Two life paths for players to choose from: Adventurer and Hacker
- Hacking encounter where a player must guess a specific pin
- Consequences for correct or wrong pin entry
- Combat encounter with options to fight or talk
- Randomized damage during combat
- Player's choices impact their empathy and humanity scores
- Winning conditions based on empathy, humanity, and opponent's defeat
- Loss conditions based on health, empathy, and humanity thresholds
- User-friendly prompts for player actions and choices
- Handling of player's turn during combat (fight or talk options)
- Handling of opponent's turn during combat (random choice to fight or talk)
- Reset character attributes to default values
- Main game loop to keep playing or restart after each round

### Visuals:
- Grid view that displays the status of both the player and the opponent, including health, empathy, and humanity values.

### Modularity:
- The code is organized into separate classes and methods, allowing for easy extension and modification.

## Features left to implement:

- Different levels of difficulty
- Multiple choices for life paths
- Multiple charackter skills
- Colorama for more colors
- Set limition of charackters for typing the name
- Set limition of charackters for typing the pin

## How to play:

#### Enter your name:
By beginning the game you need to enter a name.

![input_name](/assets/documentation/input_name.png "input_name")

#### Choose your life path:

You can choose between a adventure or a hacking game.

![lifepath](/assets/documentation/lifepath.png "lifepath")

#### Life path hacker:
The intention is to become a "real" hacker.
To be able to enter the correct pin, you have to look at the code.
If you can't hack, you should not choose this life path.
This part is meant to be fun, of course.

![hack](/assets/documentation/hack.png "hack")

#### Life path adventure:
- The player competes against the computer.
- The rules and functions are identical for the player and the computer.
- All values are randomly generated.
- The player and the computer start with 100 health each, as well as the values 15 each for empathy and humanity.
- The choice "fight" generates a hit between 5-20.
- If healt is 0, you have won respectively lost.
- Each choice for fight lowers the empathy and humanity values by 1-5.
- The empathy and humanity values interact differently with each other. 
- If both values are at 0, you have lost or won respectively.
- Each choice for "talk" increases the values for empathy and humanity between 5-20.
- If both values reach 100, you have won or lost respectively.

![adventure](/assets/documentation/adventure.png "adventure")


## Code Breakdown:

1. #### Importing Modules
- The script imports the random module to generate random numbers for various game events.

2. #### Character Class:
- The Character class defines the attributes and behaviors of characters in the game.
- Constants are defined within the class for winning and losing thresholds related to empathy and humanity.
- The __init__ method initializes a character with a name, health, empathy, and humanity.
- Methods like take_damage, change_empathy, change_humanity, is_defeated, and has_won are defined to modify and check character status.

3. #### Game Class:

- The Game class defines the main game and its interactions.
- The display_intro method displays an introductory banner using a multiline string.
- The __init__ method initializes the game and sets up the player and an opponent character (Cyber-Thug).
- The reset_game method collects the player's name and life path choice (Adventurer or Hacker) and sets up the game accordingly.
- The hack_encounter method simulates a hacking encounter where the player tries to enter a PIN code.
- The display_character_status method displays the status of a character, including health, empathy, and humanity.
- The player_turn method handles the player's turn during combat, allowing them to choose between fighting or talking.
- The opponent_turn method handles the opponent's turn during combat.
- The combat_encounter method manages the combat encounter between the player and the opponent.
- The check_end_conditions method checks if the game has reached an end condition, either a player win or an opponent win.
- The play method is the main game loop, where the player can choose to play again after winning or losing.
- The display_grid method displays character status in a tabular format.
- The display_character_status method has been modified to call the display_grid method for character status display.
- The display_intro method is a static method and doesn't operate on any instance-specific data or attributes of the Game class. It serves the purpose of displaying a game banner, which is a generic introductory message.
- Try/ except block for handle empty name input.

4. #### Main Execution:
- The script checks if it's being run directly (__name__ == "__main__") and creates an instance of the Game class.
- It then starts the game by calling the play method.

5. #### Implimentation of a Data Model:
- The code implements a data model through the Character class to manage character attributes (health, empathy, and humanity) and the Game class to handle game logic, encounters, and user interactions. It also incorporates features related to combat encounters and hacking challenges.

## Game Logic:

The flowchart visualizes the different decision options and paths of the game.

![game_logic](/assets/documentation/game_logic.png "game_logic")

## User Stories:

- As a user, I want to see an introduction to the game, so I can understand its theme and setting.
- As a user, I want to enter my name, so I can have a personalized gaming experience.
- As a user, I want to choose a life path (either "Adventurer" or "Hacker"), so I can play the game in a way that aligns with my preferred style.
- As a user, during a hack encounter, I want to guess a pin, so I can try to succeed in the hacking challenge.
- As a user, if I guess the pin incorrectly, I want to be shifted to a combat encounter, so I can continue the game in a different mode.
- As a user, during a combat encounter, I want to decide whether to fight or negotiate, so I can influence the outcome based on my choices.
- As a user, I want to see a grid display showing the current status of both my character and the opponent after each action, so I can make informed decisions in subsequent rounds.
- As a user, I want to be informed if my character's empathy or humanity reaches critical levels, so I can adjust my strategy accordingly.
- As a user, I want to know immediately if I've won or lost the game based on the set conditions, so I can either celebrate my victory or consider a different approach for my next attempt.
- As a user, after a game round ends, I want the option to play again, so I can enjoy more rounds without restarting the entire program.
- As a user, I want my character's health, empathy, and humanity to be reset at the start of each game, so I can begin every round on an even footing.
- As a user, I want the game to present unexpected choices and consequences based on my decisions.

## Testing User Stories:

Tested every user story of the game with Function > Expected result  > Action taken > Result
- Document the win/ lose scenario tests with a screenshot. To test the win/ lose scenarios, the thresholds were changed.

![testing](/assets/documentation/testing.png "testing")

##### Player win scenario 1/ Computer 0 Health

![player_heahlt_win](/assets/documentation/player_health_win.png "player_health_win")

##### Player win scenario 2/ Players Empathy 100 + Humanity 100

![player_talk_win](/assets/documentation/player_talk_win.png "player_talk_win")

##### Player win scenario 3/ Computer 0 Empathy/ 0 Humanity

![player_fight_win](/assets/documentation/player_fight_win.png "player_fight_win")

##### Computer win scenario 1/ Player 0 health

![computer_heahlt_win](/assets/documentation/computer_health_win.png "computer_health_win")

##### Computer win scenario 2/ Computers Empathy 100 + Humanity 100

![computer_talk_win](/assets/documentation/computer_talk_win.png "computer_talk_win")

##### Computer win scenario 3/ Players 0 Empathy/ 0 Humanity

![computer_fight_win](/assets/documentation/computer_fight_win.png "computer_fight_win")

#### Fun Fact:

- My mother also did a family and friends test :)

![mum_testing](/assets/documentation/mum_testing.jpg "mum_testing")

### Tested Desktop and Mobile Devices:
- Chome
- Firefox
- Andriod
- IOS

## Bugs
There was no need to test the application on a mobile device but as I do always a family and friends test, I found out, that the application isnt working on IOS.
The tester was not able to enter an input. Android instead works fine.
I get a test video for the IOS test:

IOS test gif [here](https://1drv.ms/i/s!AkY3LsFaa3smgiIP-mW0U_Kx36mU?e=huGze2)

## Validator Testing:

#### PEP8:
- The CI Python linter shows some formatting errors. Using Autopep8 reduces most of these errors. Nevertheless, I have decided to keep the current format despite the error messages.
- I have looked at some code with perfect PEP8 formatting. Such code is really nicely formatted and easy to read. From top to bottom, line by line.
Why have I decided to keep the current format? My code works fine and is easy to read. Adapting it for a perfect format takes time and can even trigger new error messages.
From a business perspective, I would never invest time, aka money, for a well-readable and functional code that can also scale without a clear technical need. Beautiful code makes sense but should also be in relation to a time/money investment.

- #### Functionality and Readability: 
- The most crucial aspect of code is its functionality and readability. If the current code works seamlessly and is easily understandable that can be a compelling reason not to alter it.

- #### Time Investment: 
- Adapting code to a perfect PEP8 format can be time-consuming, especially in larger projects. Time is a precious resource, and it's important to use it efficiently. If the code changes don't provide clear benefits, it may be more sensible to invest that time in other development activities.

- #### Potential Errors: 
- Modifying the format of a working code can introduce unexpected errors. If the code has already been well-tested, and the changes are only for format improvement, there's a risk of introducing new problems.

- #### Business Perspective: 
- In many cases, software development is a business, and resources (time and money) must be managed carefully. It's crucial for technical decisions to align with business goals. If the current code meets the requirements and is maintainable, it may be unnecessary to invest time in cosmetic changes.

- #### Without Autopep8:

![without_autopep8](/assets/documentation/without_autopep8.png "without_autopep8")

- #### With Autopep8:

![with_autopep8](/assets/documentation/with_autopep8.png "with_autopep8")

## Deploy:

#### Forking a Repo on GitHub:

- Navigate to the GitHub repo: https://github.com/renebaumann3000/Project_3
- Click the "Fork" button in the top-right corner of the repo page.
 This will create a copy of the repository under your GitHub account.
- You can then clone or download the repo as needed.
- Deploying on Heroku ->

#### Heroku Setup:

- Sign up for a Heroku account if you haven't already: https://signup.heroku.com/

#### Access Deployment Configuration:

- Once logged into Heroku, navigate to the "Deploy" section of your app's dashboard.

#### Choose Deployment Method:

- Under the deployment methods, choose "GitHub" as your preferred method.

#### Connect to GitHub:

- Ensure your connection to GitHub is confirmed.
- Use the search function provided in this section to locate your repository. In this context, the repository was named "Project_3". Once found, connect to it.

### Deployment Options:

#### Automatic Deploys: 
- By enabling this, Heroku will automatically rebuild and redeploy the app every time you push a new change to the connected GitHub repository.

#### Manual Deploy:

- If you prefer more control over when the app gets deployed and the ability to view deployment logs, you can choose the "deploy branch" option.
- When ready, you can manually initiate the deployment process for your specific branch.

## Summary and self reflection:

This project is my first step with Python.
I had fun experimenting with the language.
The short deadline for the end of the project with about 14 days unfortunately kills my creativity and happiness with the language.
The PEP8 format also triggered more problems for me than it solved. But I get that it could helpful in bigger projects and also for bigger teams to have all on the same page...
For example, I started to extend the hacking game so that the player can actually guess a pin.
Unfortunately, there is not enough time for a final integration.
In the future, though, I might expand that.

![hacking](/assets/documentation/hacking.png "hacking")


## Credits:
- ASCII Generator: https://manytools.org/hacker-tools/ascii-banner/#google_vignette
- PEP8 Formatter: https://black.vercel.app/
- Inspiration: https://en.wikipedia.org/wiki/Cyberpunk_(role-playing_game)
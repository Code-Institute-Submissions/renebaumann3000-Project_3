# Cyberpunk - A text based RPG

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

4. #### Main Execution:
- The script checks if it's being run directly (__name__ == "__main__") and creates an instance of the Game class.
- It then starts the game by calling the play method.

5. #### Implimentation of a Data Model:
- The code implements a data model through the Character class to manage character attributes (health, empathy, and humanity) and the Game class to handle game logic, encounters, and user interactions. It also incorporates features related to combat encounters and hacking challenges.


## Credits:
- ASCII Generator: https://manytools.org/hacker-tools/ascii-banner/#google_vignette
- PEP8 Formatter: https://black.vercel.app/
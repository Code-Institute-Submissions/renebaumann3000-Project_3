import random

# Defines the attributes and behaviors of a character in the game
class Character:
    # Class constants defining winning and losing thresholds
    WIN_EMPATHY_THRESHOLD = 100
    WIN_HUMANITY_THRESHOLD = 100
    LOSS_EMPATHY_THRESHOLD = 0
    LOSS_HUMANITY_THRESHOLD = 0

# Initializes character with name, health, empathy, and humanity
def __init__(self, name, health=100, empathy=15, humanity=15):
    self.name = name
    self.health = health
    self.empathy = empathy
    self.humanity = humanity

# Defines the main game and its interactions
class Game:
# Initializes game with a player and an opponent character
    def __init__(self):
    self.player = None
    self.opponent = Character("Cyber-Thug")

        def reset_game(self):
        name = input("Enter your name: ")
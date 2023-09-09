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

# Resets the game by taking player name and setting life path
def reset_game(self):
    name = input("Enter your name: ")
    self.player = Character(name)
    print(f"Welcome, {self.player.name} to Cyberpunk A text based RPG!")

        while True:
        life_path = input("Choose your life path ([A]dventurer, [H]acker): ").lower()
        if life_path in ['a', 'h']:
        return life_path
        print("Invalid choice. Please type 'A' for Adventurer or 'H' for Hacker.")


# Main game loop to keep playing or restart after each round
def play(self):
        while True:
        life_path = self.reset_game()
        if life_path == 'a':
        player_win, opponent_win = self.combat_encounter()
        elif life_path == 'h':
        player_win, opponent_win = self.hack_encounter()

        if player_win:
        prompt = "Play again? (y/n): "
        elif opponent_win:
        prompt = "Try again? (y/n): "
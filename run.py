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

            # Reduces the health of the character by the given damage
    def take_damage(self, damage):
        self.health -= damage

            # Adjusts the empathy of the character
    def change_empathy(self, delta):
        self.empathy += delta

            # Adjusts the humanity of the character
    def change_humanity(self, delta):
        self.humanity += delta

            # Checks if character is defeated based on health, empathy, and humanity
    def is_defeated(self):
        return self.health <= 0 or (self.empathy <= Character.LOSS_EMPATHY_THRESHOLD and self.humanity <= Character.LOSS_HUMANITY_THRESHOLD)

            # Checks if character has won based on empathy and humanity
    def has_won(self):
        return self.empathy >= Character.WIN_EMPATHY_THRESHOLD and self.humanity >= Character.WIN_HUMANITY_THRESHOLD

        # Defines the main game and its interactions
class Game:
    # Initializes game with a player (set later) and an opponent character
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

                # Manages the hacking encounter in the game
    def hack_encounter(self):
        print(f"{self.player.name}, you chose to hack!")
        pin = input("You have to enter a 4 digit pin.\n" "The pin is a combination of letters Aa - Zz and numbers 0-9.\n" "If the code is correct, you will win the game. If the code is incorrect, you will lose 50 Health.\n" "You only have one try. Hack or Fail!\n" "Enter the 4-digit pin: ")

                if pin == "Ren3":
            print("Hack successful! You win!")
            return True, False  # player_win, or player lose health
                    else:
            print("Hack failed. Security has detected your attempt!")
            self.player.health = 50
            return self.combat_encounter()

                # Displays the status of a given character
    def display_character_status(self, character):
        print(f"{character.name} - Health: {character.health}, Empathy: {character.empathy}, Humanity: {character.humanity}")

            # Displays the status of a given character
    def display_character_status(self, character):
        print(f"{character.name} - Health: {character.health}, Empathy: {character.empathy}, Humanity: {character.humanity}")

            # Handles the player's turn during combat
    def player_turn(self):
        while True:
            choice = input("Will you [F]ight or [T]alk? ").lower()
            if choice == "f":
                player_damage = random.randint(5, 20)
                print(f"You attack the {self.opponent.name} and deal {player_damage} damage.")
                self.opponent.take_damage(player_damage)
                self.player.change_empathy(-random.randint(1, 5))
                self.player.change_humanity(-random.randint(1, 5))
                break
                elif choice == "t":
                print("You try to negotiate.")
                self.player.change_empathy(random.randint(5, 20))
                self.player.change_humanity(random.randint(5, 20))
                break
                else:
                print("Invalid choice. Please type 'F' to Fight or 'T' to Talk.")

                # Display the opponent's status after their turn
        self.display_character_status(self.opponent)

        # Manages the combat encounter in the game
    def combat_encounter(self):
        print(f"You encounter a hostile {self.opponent.name}!")
        while True:
            self.player_turn()
            player_win, opponent_win = self.check_end_conditions()
            if player_win or opponent_win:
                return player_win, opponent_win

                self.opponent_turn()
            player_win, opponent_win = self.check_end_conditions()
            if player_win or opponent_win:
                return player_win, opponent_win

                # Checks if the game has reached an end condition
    def check_end_conditions(self):
        player_win = (self.player.empathy >= Character.WIN_EMPATHY_THRESHOLD and self.player.humanity >= Character.WIN_HUMANITY_THRESHOLD) or \
                     self.opponent.is_defeated()

        opponent_win = (self.opponent.empathy >= Character.WIN_EMPATHY_THRESHOLD and self.opponent.humanity >= Character.WIN_HUMANITY_THRESHOLD) or \
                       self.player.is_defeated()

        if player_win:
            print("You won!")
        elif opponent_win:
            print("GAME OVER! You lost!")

            return player_win, opponent_win

                

                



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

            while True:
                play_again = input(prompt).lower()
                if play_again in ['y', 'n']:
                    break
                print("Invalid choice. Please type 'y' to continue or 'n' to exit.")

            if play_again != "y":
                break


            # Checks if the script is being run directly and starts the game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play()
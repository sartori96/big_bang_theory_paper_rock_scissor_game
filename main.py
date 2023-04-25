"""Paper Rock Scissor Game Project"""
import random

PLAY = {
    "Spock": "🖖",
    "Rock": "👊",
    "Paper": "✋",
    "Scissor": "✌️",
    "Lizard": "🦎"
}
WINNING_PLAYS = {
    "Scissor": ["Lizard", "Paper"],
    "Rock": ["Scissor", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Rock", "Scissor"]
}


class PaperRockScissorGame:

    def __init__(self):
        self.player = ""
        self.print_welcome_message()
        self.run()

    def print_welcome_message(self):
        print("Welcome to the Paper Rock Scissors Game!")
        print("You will be playing against the computer.")

    def run(self):
        while True:
            self.input_player_choice()
            message = self.verifications_game()
            if isinstance(message, str):
                print(message)
            else:
                break

    def input_player_choice(self):
        self.player = str(
            input("Please select one of the following options: Spock, Rock, Paper, Scissor, Lizard."
                  " To quit the game, type exit and press enter. \nYou play: ")).title()

    def verifications_game(self) -> bool or str:

        if self.player == "Exit":
            return False
        if self.player not in PLAY:
            return "You typed an invalid command, you lose!"

        pc_play = str(random.choice(list(PLAY.keys())))

        print(f"And the Computer plays: {pc_play}\n{PLAY[self.player]} vs {PLAY[pc_play]}")

        if self.player == pc_play:
            return "It's a draw =T"
        elif pc_play in WINNING_PLAYS[self.player]:
            return "You win! xD"
        else:
            return "You lose =/"


if __name__ == "__main__":
    paper_rock_scissor_game = PaperRockScissorGame()

"""
This module defines a Game class that creates a random grid of letters and checks if a given word
can be formed with the letters in the grid, considering each letter's frequency in the grid.
"""

import random
from collections import Counter


class Game:
    """
        Initializes the Game object with a random grid of uppercase letters.
        The grid is of size 9 by default.
    """

    def __init__(self) -> None:
        self.size = 9
        self.grid = self.generate_grid()


    def generate_grid(self):
        """Generates a new random grid of uppercase letters."""
        return [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(self.size)]


    def is_valid(self, word: str) -> bool:
        """Check if the provided word can be formed from the letters in the game's grid."""
        if not word:
            return False
        word_count = Counter(word)
        grid_count = Counter(self.grid)
        return all(word_count[letter] <= grid_count[letter] for letter in word)


    def display_grid(self):
        """Display the grid in a formatted output."""
        print("Current Grid:", ''.join(self.grid))


    def reset_grid(self):
        """Resets the grid with new random letters."""
        self.grid = self.generate_grid()


# Example usage:
# game = Game()
# game.display_grid()
# print(game.is_valid("HELLO"))  # Output depends on the random grid
# game.reset_grid()
# game.display_grid()



# Example usage:
# game = Game()
# print(game.is_valid("HELLO"))  # Output depends on the random grid

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
        self.grid = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(self.size)]
        self.dictionary = self.load_dictionary()


    def load_dictionary(self):
        """Generates a new random grid of uppercase letters."""
        return {'KNOWN', 'WORD', 'ANOTHER', 'VALID', 'WORDS'}


    def is_valid(self, word: str) -> bool:
        """
        Check if the word can be formed from the letters in the game's grid,
        is longer than 3 characters, and is in the dictionary.
        """
        if not word or len(word) <= 3 or word.upper() not in self.dictionary:
            return False
        word_count = Counter(word.upper())
        grid_count = Counter(self.grid)
        return all(word_count[letter] <= grid_count[letter] for letter in word)



# Example usage:
# game = Game()
# game.display_grid()
# print(game.is_valid("HELLO"))  # Output depends on the random grid
# game.reset_grid()
# game.display_grid()

# Example usage:
# game = Game()
# print(game.is_valid("HELLO"))  # Output depends on the random grid

# new_game = Game()
# new_game.grid = list('KWIENFUQW')
# print(new_game.is_valid('FEUN'))
# => true

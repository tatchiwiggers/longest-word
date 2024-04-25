"""
    This module contains the Game class, which manages a grid of randomly chosen uppercase letters.
    The Game class provides functionality to validate if a specific word can be formed from the
    letters in the grid, with each letter in the grid usable only once per validation.
"""


import string
import random


class Game:
    """
    A simple game class that manages a grid of randomly chosen uppercase letters.

    Attributes:
        grid (list of str): A list containing single uppercase letters.
    """

    def __init__(self):
        """
        Initializes a new game instance by populating the rid with nine random
        uppercase letters.
        """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """
        Checks if the provided word can be formed with the letters currently in
        the grid. Each letter in the grid
        can only be used once per word validation call.

        Args:
            word (str): The word to check against the grid.

        Returns:
            bool: True if the word can be formed using the letters in the
                  rid without reuse within the word,
                  False otherwise.
        """
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True


    def reset_grid(self):
        """
        Resets the grid to a new set of nine random uppercase letters.
        """

        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def display_grid(self):
        """
        Displays the current state of the grid.
        """

        return ' '.join(self.grid)

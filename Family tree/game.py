# game.py

class GotCharacter:
    """Base class for a Game of Thrones character"""
    
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self):
        status = "alive" if self.is_alive else "dead"
        return f"{self.first_name} is {status}"


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Prints the House words"""
        print(self.house_words)

    def die(self):
        """Kills the character (sets is_alive to False)"""
        self.is_alive = False

    def __str__(self):
        status = "alive" if self.is_alive else "dead"
        return f"{self.first_name} {self.family_name} is {status} - House words: {self.house_words}"

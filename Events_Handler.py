
from coffee_hangman import Coffee_Hangman
from random import randint

class EventHandler:

    def hang_man(self, root):
        if Coffee_Hangman.initialize(Coffee_Hangman, root):
            return True
        else:
            return False
    def random_events(self, root):
        chance = randint(1, 1000000)
        if chance == 1000000:
            result = self.hang_man(Coffee_Hangman, root)
            if result:
                return 10000
            
            else:
                return 0
        else:
            return 0


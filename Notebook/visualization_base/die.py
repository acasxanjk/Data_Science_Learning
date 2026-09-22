from random import randint

class Die:
    """Class representing a die"""
    def __init__(self,num_sides=6):
        """Dice have six sides by default."""
        self.num_sides = num_sides

    def roll(self):
        """Returns a value between one and the number of dice rolls."""
        return randint(1,self.num_sides)




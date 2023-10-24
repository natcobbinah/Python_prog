import random

class Die:
    """Simulating a dice roll"""
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
      randomValue = random.randint(1,self.sides)
      print(f"The random value is {randomValue}")
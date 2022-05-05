import random

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        x = random.randint(1,self.sides)
        return x

die =Die()
for i in range(10):
    print(die.roll_die())
    
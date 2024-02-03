import random

class RandomQueue():
    def __init__(self, choices, min_dist):
        if type(choices) != list:
            raise Exception("The choices must be a list")
        if min_dist >= len(choices):
            raise Exception("The minimum distance must the lower than the number of elements in the choices list")
        if type(min_dist) != int or min_dist < 0:
            raise Exception("The minimum distance must be a positive integer")
        self.choices = choices
        self.min_dist = min_dist

        self.counters = [0 for _ in choices]

    def getChoice(self):
        self.counters = list(map(lambda n: n - 1 if n > 0 else 0, self.counters))

        possible = dict()
        for index,(choice, counter) in enumerate(zip(self.choices,self.counters)):
            if counter == 0:
                possible[index] = choice

        randn = random.randint(0, len(possible) - 1)
        index = list(possible.keys())[randn]

        self.counters[index] = self.min_dist + 1
        
        return possible[index]
    


    

    
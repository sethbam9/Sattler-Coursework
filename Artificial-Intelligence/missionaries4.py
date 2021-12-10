import random 
import statistics
from copy import deepcopy 
from time import process_time, sleep

class Game:

    def __init__(self):
        self.missionaries = 3
        self.cannibals = 3
        self.origin = [self.missionaries, self.cannibals]
        self.destination = [3 - self.missionaries, 3 - self.cannibals]
        self.visited = []
        self.round = 0

    def get_options(self, loc): 
        m = [1, 0] if loc[0] > 0 else None
        mm = [2, 0] if loc[0] > 1 else None
        c = [0, 1] if loc[1] > 0 else None
        cc = [0, 2] if loc[1] > 1 else None
        mc = [1, 1] if m and c else None

        options = [i for i in [m, mm, c, cc, mc] if i]

        return options

    def transport(self, loc):
        dest = self.destination if self.round % 2 == 0 else self.origin
        options = self.get_options(loc)
        choices = []
        for option in options:
            missionaries = loc[0] - option[0]
            cannibals = loc[1] - option[1]
            if missionaries in [0, cannibals, 3]:
            # and [missionaries, cannibals] not in self.visited \
                # or option == options[-1]:
                choices.append(option)

        boat = random.choice(choices)

        loc[0] -= boat[0]
        loc[1] -= boat[1]
        dest[0] += boat[0]
        dest[1] += boat[1]

        if [loc[0], loc[1]] not in self.visited:
            self.visited.append([loc[0], loc[1]])
        # print(self.round, self.origin, self.destination)


    def play(self):
        self.origin = [self.missionaries, self.cannibals]
        self.destination = [3 - self.missionaries, 3 - self.cannibals]
        self.round = 0
        while True:
            self.transport(self.origin)
            self.round += 1
            
            if sum(self.origin) == 0:
                return self.round 

            self.transport(self.destination)
            self.round += 1


def stats():
    avg = []
    run_time = process_time()
    for i in range(1000):
        avg.append(Game().play())
    print("Avg: ", statistics.mean(avg))
    print("Max: ", max(avg))
    print("Min: ", min(avg))
    print("Time: ", run_time + process_time())

stats() 
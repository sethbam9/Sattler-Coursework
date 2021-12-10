import random 
import statistics
from copy import deepcopy 
from time import process_time

left = ["m", "m", "m", "c", "c", "c"]
right = []

def get_options(loc, count, boatL):
    countM, countC = loc.count("m"), loc.count("c")
    
    missionary = ["m"] if countM > 0 else None
    missionaries = ["m", "m"] if countM > 1 else None
    cannibal = ["c"] if countC > 0 else None
    cannibals = ["c", "c"] if countC > 1 else None
    both = ["m", "c"] if countM > 1 and countC > 1 else None
    
    options = [i for i in 
        [missionary, missionaries, cannibal, cannibals, both] 
        if i != None]

    # if count == 0:
    #     options =[cannibals, both]

    global left, right
    # if not boatL and right.count("m") > 2: 
    #     options = [cannibal]
    # elif boatL and left.count("m") < 1 and left.count("c") > 1:
    #     options = [cannibals] 

    return options
     

def transfer_passangers(locA, locB, count):
    boatL = True if count % 2 == 0 else False
    options = get_options(locA, count, boatL)

    while True:
        loc_a, loc_b = deepcopy(locA), deepcopy(locB)
        passangers = random.choice(options)

        for passanger in passangers:
            loc_a.remove(passanger)
            loc_b.append(passanger)

        countA = loc_a.count("m") - loc_a.count("c")
        countB = loc_b.count("m") - loc_b.count("c")
        countR = len(loc_b) if boatL else len(loc_a)

        if (countA >= 0 or loc_a.count("m") < 1) and \
        (countB >= 0 or loc_b.count("m") < 1): # and countR > 0:
            global left, right
            if boatL:
                left, right = loc_a, loc_b 
            else: 
                left, right = loc_b, loc_a

            return passangers

        options.remove(passangers)


def missionaries():
    count = 0
    # print(left, right)
    while True:
        # print(count, left, right)
        transfer_passangers(left, right, count)
        count+=1

        # print(count, left, right)
        if len(right) == 6: 
            return count
        
        transfer_passangers(right, left, count)
        count+=1


def stats():
    global left, right
    avg = []
    l, r = deepcopy(left), deepcopy(right)
    run_time = process_time()
    for i in range(1000):
        left, right = l, r
        avg.append(missionaries())
    print("Avg: ", statistics.mean(avg))
    print("Max: ", max(avg))
    print("Min: ", min(avg))
    print("Time: ", run_time + process_time())

stats() 
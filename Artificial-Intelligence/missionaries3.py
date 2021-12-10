import random 
import statistics
from copy import deepcopy 
from time import process_time, sleep

origin = [3, 3]

def m_depart(l, n):
    l[0] -= n 

def c_depart(l, n):
    l[1] -= n 
    
def pair_depart(l, n):
    m_depart(l, n)
    c_depart(l, n)

def m_return(l, n):
    l[0] += n 

def c_return(l, n):
    l[1] += n 

def pair_return(l, n):
    m_return(l, n)
    c_return(l, n)

def get_options(l, options):
    options_copy = deepcopy(options)
    for i in range(len(options)):
        count = deepcopy(l)
        options[i][0](count, options[i][1])
        if count[0] < 0 or count[1] < 0 or count[0] > 3 or count[1] > 3:
            options_copy.remove(options[i])

    return options_copy 


def depart(l):
    count = deepcopy(l)
    dep_options = [[m_depart, 1], [m_depart, 2],
    [c_depart, 1], [c_depart, 2], [pair_depart, 1]]
    options = get_options(count, dep_options)

    while True:
        count = deepcopy(l)
        departure = random.choice(options)
        departure[0](count, departure[1])
        if (count[0] == count[1]) or (count[0] == 0) or (count[0] == 3):
            return count

        options.remove(departure)

        
def returnal(l):
    count = deepcopy(l)
    ret_options = [[m_return, 1], [m_return, 2],
    [c_return, 1], [c_return, 2], [pair_return, 1]]
    options = get_options(count, ret_options)

    while True:
        count = deepcopy(l)
        returnal = random.choice(options)
        returnal[0](count, returnal[1])
       
        if (count[0] == count[1]) or (count[0] == 0) or (count[0] == 3):
            return count

        options.remove(returnal)

def missionaries(l):
    steps = 0
    # print(steps, l)
    while True:
        l = depart(l)
        steps += 1
        # print(steps, l)

        if l[0] == 0 and l[1] == 0: return steps

        l = returnal(l)
        steps += 1
        # print(steps, l)

# missionaries(origin)

def stats():
    avg = []
    run_time = process_time()
    for i in range(1000):
        l = [3,3]
        avg.append(missionaries(l))
    print("Avg: ", statistics.mean(avg))
    print("Max: ", max(avg))
    print("Min: ", min(avg))
    print("Time: ", run_time + process_time())

stats() 


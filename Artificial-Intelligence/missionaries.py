m = ["m1", "m2", "m3"]
c = ["c1", "c2", "c3"]
A = {"m":m, "c":c}
B = {"m":[], "c":[]}

import random
import time
import copy

def my_try(key, index):
    try:
        option = key[index]
    except IndexError:
        return None
    return option

def options(loc, id, count):
    m = my_try(loc["m"], 0)
    c = my_try(loc["c"], 0)

    mc = None
    if m and c:
        mc = [m, c]

    mm = None
    if m:
        m2 = my_try(loc["m"], 1)
        if m2:
            mm = [m, m2]

    cc = None
    if c:
        c2 = my_try(loc["c"], 1)
        if c2:
            cc = [c, c2]

    options = [i for i in [m, c, mc, mm, cc] if i != None]
    if count == 0:
        options.remove(m)
        options.remove(c)

    # if id == "b" and len(loc["m"]) == 3:
    #     options = [c]
    # elif id == "a" and len(loc["m"]) == 0 and len(loc["c"]) > 1:
    #     options = [cc]

    return options

def transfer_passangers(passanger, loc_a, loc_b):
    # transfer missionary
    if passanger[0] == "m":
        loc_a["m"].remove(passanger)
        loc_b["m"].append(passanger)
    # transfer cannibal
    else:
        loc_a["c"].remove(passanger)
        loc_b["c"].append(passanger)

def transport(loc_A, loc_B, id, count):
    while True:
        loc_a = copy.deepcopy(loc_A)
        loc_b = copy.deepcopy(loc_B)
        passangers = random.choice(options(loc_a, id, count))

        if isinstance(passangers, list):
            for passanger in passangers:
                transfer_passangers(passanger, loc_a, loc_b)
        
        else:
            transfer_passangers(passangers, loc_a, loc_b)

        # count missionaries and cannibals at each location
        m_A = len(loc_a["m"])
        c_A = len(loc_a["c"])
        m_B = len(loc_b["m"])
        c_B = len(loc_b["c"])

        if id != "a":
            temp1 = m_A
            temp2 = c_A
            m_A = m_B
            m_B = temp1
            c_A = c_B
            c_B = temp2

        legal_A = False
        if (m_A >= c_A) or m_A == 0:
            legal_A = True

        legal_B = False
        if (m_B >= c_B) or m_B == 0:
            legal_B = True

        count_R = m_B + c_B

        if (legal_A and legal_B and count_R > 0): # also add and count_R > 0
            # print("O", options(loc_A))
            global A, B
            if id == "a":
                A = loc_a
                B = loc_b
            else:
                B = loc_a
                A = loc_b
            return passangers
    

def missionaries():
    count = 0
    # print(f"{count}, A: {A['m']+A['c']} B: {B['m']+B['c']}")
    while True:
        passangers = transport(A, B, "a", count)
        # print(f"{count}, A: {A['m']+A['c']} -> \_{passangers}_/ -> B: {B['m']+B['c']}")
        count += 1

        if len(A["m"] + A["c"]) == 0:
            return count

        passangers = transport(B, A, "b", count)
        # print(f"{count}, A: {A['m']+A['c']} <- \_{passangers}_/ <- B: {B['m']+B['c']}")
        count+=1

import statistics
def stats():
    global A, B
    avg = []
    dA, dB = copy.deepcopy(A), copy.deepcopy(B)
    run_time = time.process_time()
    for i in range(1000):
        A, B = dA, dB
        avg.append(missionaries())
    print("Avg: ", statistics.mean(avg))
    print("Max: ", max(avg))
    print("Min: ", min(avg))
    print("Time: ", run_time + time.process_time())

stats()













# http://ais.informatik.uni-freiburg.de/teaching/ss11/ki/exercises/search.py
from copy import deepcopy
from collections import deque
import sys
import time

# Within this object, the state is represented as described in the lecture:
# The triple (m,c,b) holds the number of missionaries, cannibals and boats
# on the original shore.
class State(object):
  def __init__(self, missionaries, cannibals, boats):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boats = boats
  
  def successors(self):
    if self.boats == 1:
      sgn = -1
      direction = "from the original shore to the new shore"
    else:
      sgn = 1
      direction = "back from the new shore to the original shore"
    for m in range(3):
      for c in range(3):
        newState = State(self.missionaries+sgn*m, self.cannibals+sgn*c, self.boats+sgn*1);
        if m+c >= 1 and m+c <= 2 and newState.isValid():    # check whether action and resulting state are valid
          action = "take %d missionaries and %d cannibals %s. %r" % ( m, c, direction, newState) 
          yield action, newState
            
  def isValid(self):
    # first check the obvious
    if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3 or (self.boats != 0 and self.boats != 1):
      return False   
    # then check whether missionaries outnumbered by cannibals
    if self.cannibals > self.missionaries and self.missionaries > 0:    # more cannibals then missionaries on original shore
      return False
    if self.cannibals < self.missionaries and self.missionaries < 3:    # more cannibals then missionaries on other shore
      return False
    return True

  def is_goal_state(self):
    return self.cannibals == 0 and self.missionaries == 0 and self.boats == 0

  def __repr__(self):
    return "< State (%d, %d, %d) >" % (self.missionaries, self.cannibals, self.boats)



class Node(object):  
  def __init__(self, parent_node, state, action, depth):
    self.parent_node = parent_node
    self.state = state
    self.action = action
    self.depth = depth
  
  def expand(self):
    for (action, succ_state) in self.state.successors():
      succ_node = Node(
                       parent_node=self,
                       state=succ_state,
                       action=action,
                       depth=self.depth + 1)
      yield succ_node
  
  def extract_solution(self):
    solution = []
    node = self
    while node.parent_node is not None:
      solution.append(node.action)
      node = node.parent_node
    solution.reverse()
    return solution


def breadth_first_tree_search(initial_state):
  initial_node = Node(
                      parent_node=None,
                      state=initial_state,
                      action=None,
                      depth=0)
  fifo = deque([initial_node])
  num_expansions = 0
  max_depth = -1
  while True:
    if not fifo:
      print("%d expansions" % num_expansions)
      return None
    node = fifo.popleft()
    if node.depth > max_depth:
      max_depth = node.depth
      print("[depth = %d] %.2fs" % (max_depth, time.process_time()))
    if node.state.is_goal_state():
      print("%d expansions" % num_expansions)
      solution = node.extract_solution()
      return solution
    num_expansions += 1
    fifo.extend(node.expand())


def usage():
  print >> sys.stderr, "usage:"
  print >> sys.stderr, "    %s" % sys.argv[0]
  raise SystemExit(2)


def main():
  initial_state = State(3,3,1)
  solution = breadth_first_tree_search(initial_state)
  if solution is None:
    print("no solution")
  else:
    print("solution (%d steps):" % len(solution))
    for step in solution:
      print("%s" % step)
  print("elapsed time: %.2fs" % time.process_time())


# for i in range(1000):
#     main()
q = [1,2,3]
pop = q.pop()
print(pop)

# Page 67
def simpProbSolvAgent(percept):
    sequence = []
    state = 0
    goal = None
    problem = 0
    state = updateState(state, percept)
    if not sequence:
        goal = formulateGoal(state)
        problem = formulateProblem(state, goal)
        sequence = search(problem)
        if not sequence:
            return None #Failure
    action = sequence[0]
    sequence = sequence[1:]
    return action 

def updateState(state, percept):
    pass

def formulateGoal(state):
    pass

def formulateProblem(state, goal):
    pass 

def search(problem):
    pass

# Page 77
def treeSearch(problem):
    frontier = problem[0]
    while True:
        if not frontier:
            return None #Failure
        node = chooseLeaf(frontier)
        if goal_state in node:
            return solution
        frontier = node.expand()


def graphSearch(problem):
    frontier = problem[0]
    explored = ()
    while True:
        if not frontier:
            return None #Failure
        node = chooseLeaf(frontier)
        if goal_state in node:
            return solution
        explored.insert(node)
        if node not in frontier or explored:
            frontier = node.expand()
        
def chooseLeaf(frontier):
    pass 

class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent 
        self.action = action
        self.path_cost = path_cost

def childNode(problem, parent, action):
    node = Node(
        problem.result(parent.state, action),
        parent,
        action, 
        parent.path_cost)
    return node
    
# Page 82
def breadthFirstSearch(problem):
    node = Node(problem.intial_state, None, None, 0)
    if problem.goalTest(node.state):
        return solution(node)
    frontier = [node]
    explored = ()
    while True:
        if not frontier:
            return None #Failure
        node = frontier.pop()
        explored.insert(node.state)
        for action in problem.actions(node.state):
            child = childNode(problem, node, action)
            if child.state not in explored or frontier:
                if problem.goalTest(child.state):
                    return solution(child)
                frontier.append(child)
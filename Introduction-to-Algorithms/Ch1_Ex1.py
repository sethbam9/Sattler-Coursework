
# Creates an empty stack.
def CreateStack():
    S = []
    return S

# Pushes item i on the top of stack S.
def Push(S, i):
    return S.append(i)


# Gives the value of the item on top of stack S w/o removing it.
def Top(S):
    return S[len(S) - 1]

# Pops the item on the top of the stack.
def Pop(S):
    return S.pop()

# Returns TRUE if stack S is empty.
def IsStackEmpty(S):
    if len(S) == 0:
        return True

# Returns stack S's size.
def Size(S):
    return len(S)

# Returns TRUE if stack S is full.
def Full(S):
    if len(S) == 5:
        return True


# Applying the Functions

spans = [1]
prices = [1, 3, 2, 4]
S = CreateStack()
Push(S, 0)
i = 1
while i < len(prices):
    while not IsStackEmpty(S) and \
    prices[Top(S)] <= prices[i]:
        Pop(S)
    if IsStackEmpty(S):
        spans.append(i + 1)
    else:
        spans.append(i - Top(S))
    Push(S, i)
    i += 1
print(spans)

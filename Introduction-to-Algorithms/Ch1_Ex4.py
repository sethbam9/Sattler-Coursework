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

# Bracket reader:
items = ['(', '{', '[', ']', ')', ')', ']']
S = CreateStack()
L = ['(', '{', '[']
R = []
i = 0

while i < len(items):
    if items[i] in L:
        Push(S, items[i])
    else:
        R.append(items[i])
    i += 1

i = 0
while i < len(R):
    if Top(S) == '(' and R[i] == ')':
        Pop(S)
    elif Top(S) == '[' and R[i] == ']':
        Pop(S)
    elif Top(S) == '{' and R[i] == '}':
        Pop(S)
    else:
        print("Unbalanced")
        exit(0)
    i += 1

print("Balanced")

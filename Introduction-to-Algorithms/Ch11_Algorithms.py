import csv
import random
import time

# Algorithm 11.2: Self-organizing search with move-to-front (p. 260)
def MoveToFrontSearch(L, s):
    p = None
    for r in L:
        if r == s:
            if p != None:
                L.remove(r)
                L.insert(0, r)
                # print("Move to Front:\n", L.index("unicorn"))
                return r
            return r
        p = r
    return None

# Algorithm 11.3: Self-organizing search with transposition (p. 261)
def TranspositionSearch(L, s):
    p = None
    q = None
    for r in L:
        if r == s:
            if p != None:
                L.remove(r)
                L.insert(L.index(q), r)
                # print("Transposition:\n", L)
                return r
            return r
        q = p
        p = r
    return None

# Algorithm 11.4: Self-organizing search with the transposition method in an array (p. 262)
def Swap(A, i, a, b):
    A[i-1] = str(b)
    A[i] = a

def TranspositionArraySearch(A, s):
    for i in range(len(A)):
        if A[i] == s:
            if i > 0:
                Swap(A, i, A[i - 1], A[i])
                # print("Transposition Array:\n", A)
                return i - 1
            else:
                return i
    return None

# Algorithm 11.5 (p. 264)
def Compare(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0

def SecretarySearch(A):
    e = 2.7182
    m = int(len(A) / e)
    c = 0
    for i in range(m):
        if Compare(A[i], A[c]) > 0:
            c = i
    for i in range((m + 1), len(A)):
        if Compare(A[i], A[c]) > 0:
            A[i] = str(A[i])
            # print("Secretary:\n", A)
            return i
    return None

# Algorithm 11.7: Safe binary search without overﬂows.
def SafeBinarySearch(A, s):
    l = 0
    h = len(A)
    while l <= h:
        m = l + int((h - l) / 2)
        c = Compare(A[m], s)
        if c < 0:
            l = m + 1
        elif c > 0:
            h = m - 1
        else:
            # print("Safe Binary:\n", A[m])
            return A[m]
    return None

# Make csv dictionary. ----------------------------------------------------------------------
# English dictionary from https://github.com/dwyl/english-words/blob/master/words.txt
f = open(r"C:\Users\sethb\Downloads\english-words-master\english-words-master\words.txt")
file = f.read()

def MakeList():
    dictionary = []
    word = ""
    for i in file:
        if i != "\n":
            word += i
        else:
            dictionary.append(word)
            word = ""
    with open('English dictionary.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in dictionary:
            writer.writerow([val])


# LISTS ------------------------------------------------------------------------------
# with open("English dictionary.csv", newline="\n") as csvfile:
#     reader = csv.reader(csvfile)
#     data = list(reader)

# import itertools
# dict = list(itertools.chain(*data))

nums = [i for i in range(5000 ** 2)]
n2 = [nums for i in range(5)]

functions = [MoveToFrontSearch,       #0
            TranspositionSearch,      #1
            TranspositionArraySearch, #2
            SecretarySearch,          #3
            SafeBinarySearch]         #4

# MAIN FUNCTION --------------------------------------------------------------------
# f = function; l = list; i = item
def Main(f, l, i):
    start_time = time.thread_time()
    if functions[f] != SecretarySearch:
        functions[f](l, i)
    elif functions[f] == SecretarySearch:
        functions[f](l)
    print("%s: %s seconds" % (functions[f].__name__, (time.thread_time() - start_time)))

j = 4

Main(j, nums, 18947914)
# Main(j, dict, 'unicorn')

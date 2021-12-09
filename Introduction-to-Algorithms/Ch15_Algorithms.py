# Algorithm 15.1: Brute force string search.
#  A pattern p and a text t.
def bruteForceStringSearch(p, t):
    queue = []
    lp = len(p)
    lt = len(t)
    for i in range(lt-lp):
        j = 0
        while j < lp and p[j] == t[i+j]:
            j += 1
        if j == lp:
            queue.append(i)
    return queue


# Algorithm 15.3: Find the borders of a string.
def findBorders(p):
    lp = len(p)
    b = [None] * (lp+1)
    j = 0
    b[0] = j
    b[1] = j
    for i in range(1, lp):
        while j > 0 and p[j] != p[i]:
            j = b[j]
        if p[j] == p[i]:
            j += 1
        b[i+1] = j
    return b

# Algorithm 15.2: Knuth-Morris-Pratt.
def knuthMorrisPratt(p, t):
    queue = []
    lp = len(p)
    lt = len(t)
    b = findBorders(p)
    j = 0
    for i in range(lt):
        while j > 0 and p[j] != t[i]:
            j = b[j]
        if p[j] == t[i]:
            j += 1
        if j == lp:
            queue.append(i - j + 1)
            j = b[j]
    return queue


# Algorithm 15.4: Create rightmost occurrences table.
# size s of alphabet.
def createRtOccurrencesTable(p, s):
    right = [None] * s
    lp = len(p)
    for i in range(s):
        right[i] = lp
    for i in range(lp-1):
        right[ord(p[i])] = lp - i - 1
    return right


# Algorithm 15.5: Boyer-Moore-Horspool.
def boyerMooreHorspool(p, t, s=128):
    queue = []
    lp = len(p)
    lt = len(t)
    right = createRtOccurrencesTable(p, s)
    i = 0
    while i <= (lt - lp):
        j = lp-1
        while j >= 0 and t[i+j] == p[j]:
            j -= 1
        if j < 0:
            queue.append(i)
        c = t[i + lp - 1]
        i = i + right[ord(c)]
    return queue

from Ch15_text import str
print(bruteForceStringSearch("blue", str))
print(knuthMorrisPratt("blue", str))
print(boyerMooreHorspool("blue", str))

"""
Implement algorithms for ch. 15
Chapter 3, 3.2, 3.4, 3.5, 3.7
"""

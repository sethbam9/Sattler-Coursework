import random
import copy

print_all_exercises = False

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * EXERCISE 1 * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Algorithm 12.8: Merge sort. 314
def mergeSort(A):
    mergeSortHelper(A, 0, len(A) - 1)
    return A

def mergeSortHelper(A, low, high, i=0):
    str = ''
    bar = '  |'
    line = '--'
    space = '  '

    for j in range(i):
        if j < i-1:
            str = str + bar + space
        else:
            str = str + bar + line

    print(str+'sort', A[low:high+1])

    if low < high:
        mid = low + (high - low) // 2
        mergeSortHelper(A, low, mid, i+1)
        mergeSortHelper(A, mid+1, high, i+1)

        if i == 0:
            str = bar + line
        else:
            str = bar + space
        for j in range(i):
            if j < i-1:
                str = str + bar + space
            else:
                str = str + bar + line

        arrayMergeInPlace(A, low, mid, high, str)

# Algorithm 12.7: In-place array merge. 309
def arrayMergeInPlace(A, low, mid, high, tab):
    C = [0 for i in range(high - low + 1)]

    for k in range(low, high + 1):
        C[k-low] = A[k]

    i = 0
    cm = mid - low + 1
    ch = high - low + 1
    j = cm

    merge_a = A[low:mid+1]
    if len(A[mid+1:high+1]) >= 1:
        merge_b = A[mid+1:high+1]
    else:
        merge_b = [A[mid+1:high+1]]

    for k in range(low, high + 1):
        if i >= cm:
            A[k] = C[j]
            j += 1
        elif j >= ch:
            A[k] = C[i]
            i += 1
        elif C[i] <= C[j]:
            A[k] = C[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1

    print(tab+'merge', merge_a, merge_b, '-->', A[low:high+1])



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * EXERCISE 3 * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Algorithm 12.7: In-place array merge. 309
def arrayMergeInPlace2(A, low, mid, high):
    C = copy.deepcopy(A)
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i >= mid+1:
            A[k] = C[j]
            j += 1
        elif j >= high+1:
            A[k] = C[i]
            i += 1
        elif C[i] <= C[j]:
            A[k] = C[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1

def mergeSort2(A):
    mergeSortHelper2(A, 0, len(A) - 1)
    return A

def mergeSortHelper2(A, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSortHelper2(A, low, mid)
        mergeSortHelper2(A, mid+1, high)
        arrayMergeInPlace2(A, low, mid, high)



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * EXERCISE 4 * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

ex4 = """
Selection and insertion sort are quicker than merge sort until lists
surpass about the length of 100 (see 'Ch12_Algorithms.py').

Average of 10,000 runs on a list length 10:
['selectionSort', 'Avg: 9.375e-06']
['insertionSort', 'Avg: 3.125e-06']
['mergeSort',     'Avg: 3.28125e-05']

Average of 10,000 runs on a list length 100:
['selectionSort', 'Avg: 0.00019375']
['insertionSort', 'Avg: 0.000334375']
['mergeSort',     'Avg: 0.0002578125']

Average of 1,000 runs on a list length 1,000:
['selectionSort', 'Avg: 0.02009375']
['insertionSort', 'Avg: 0.03959375']
['mergeSort',     'Avg: 0.00278125']

"""



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * EXERCISE 6 * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def mergeSort3(A):
    mergeSortHelper3(A, 0, len(A) - 1)
    return A

def mergeSortHelper3(A, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSortHelper3(A, low, mid)
        mergeSortHelper3(A, mid+1, high)
        arrayMergeInPlace3(A, low, mid, high)

# Algorithm 12.7: In-place array merge. 309
def arrayMergeInPlace3(A, low, mid, high):
    C = [0 for i in range(high - low + 1)]
    for k in range(low, high + 1):
        C[k-low] = A[k]
    i = 0
    cm = mid - low + 1
    ch = high - low + 1
    j = cm
    for k in range(low, high + 1):
        if i >= cm:
            A[k] = C[j]
            j += 1
        elif j >= ch:
            A[k] = C[i]
            i += 1
        elif C[i] < C[j]:
            A[k] = C[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1

# https://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

def sortTester(n):
    for i in range(n):
        nums = [i for i in range(0, 10000, random.randint(1, 10))]
        random.shuffle(nums)
        mergeSort3(nums)
        if not is_sorted(nums):
            return print(False)

sortTester(100)

ex6 = """
Yes, when we change to a strict comparision (<) for the second elif statement
the algorithm is still reliable, which can be evidenced by the sortTester fxn.
"""



# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * EXERCISE 8 * * * * * * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# Algorithm 12.9: Quicksort. 318
def quickSort(A):
    quickSortHelper(A, 0, len(A) - 1)
    return A

def quickSortHelper(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quickSortHelper(A, low, p-1)
        quickSortHelper(A, p+1, high)

# Algorithm 12.10: Partitioning. 319
def partition(A, low, high):
    p = (low + high) // 2
    A[p], A[high] = A[high], A[p]
    b = low
    for i in range(low, high):
        if A[i] < A[high]:
            A[i], A[b] = A[b], A[i]
            b += 1
    A[high], A[b] = A[b], A[high]
    return b


#  ARRAYS
array = [i for i in range(20)]
random.shuffle(array)
array2 = copy.deepcopy(array)
nums = [84,64,37,92,2,98,5,35,70,52,73,51,88,47]

print_all_exercises = True

if print_all_exercises == True:
    print("EXERCISE 1:\n")
    mergeSort(nums)
    print("\n\n")
    print("EXERCISE 3:\n\n", mergeSort2(array), "\n\n")
    print("EXERCISE 4:\n", ex4, "\n")
    print("EXERCISE 6:\n", ex6, "\n\n")
    print("EXERCISE 7:\n")
    print(quickSort(array2), "\n")

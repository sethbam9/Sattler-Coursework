import random
import time
import copy

# Algorithm 12.1: Selection sort. 287 -------------------------------------------------
def selectionSort(A):
    for i in range(len(A) - 1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A


# Algorithm 12.2: Selection sort with no unnecessary exchanges. 289 ---------------------
def selectionSortCE(A):
    for i in range(len(A) - 1):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j
        if i != min:
            A[i], A[min] = A[min], A[i]
    return A


# Algorithm 12.3: Insertion sort. 291 ----------------------------------------------------
def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A


# Algorithm 12.5: Heapsort. 300 -----------------------------------------------------
def heapSort(A):
    items = len(A)
    for i in range((items - 1) // 2, -1, -1):
        sink(A, i, items)
    while items > 0:
        A[0], A[items-1] = A[items-1], A[0]
        items -= 1
        sink(A, 0, items)
    return A

# Algorithm 12.4: sink. 299
def sink(A, i, items):
    k = i
    placed = False
    j = k*2 + 1
    while not placed and j < items:
        if j < items-1 and A[j] < A[j+1]:
            j += 1
        if A[k] >= A[j]:
            placed = True
        else:
            A[k], A[j] = A[j], A[k]
        k = j
        j = 2*k + 1


# Algorithm 12.8: Merge sort. 314 -------------------------------------------------------
def mergeSort(A):
    mergeSortHelper(A, 0, len(A) - 1)
    return A

def mergeSortHelper(A, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSortHelper(A, low, mid)
        mergeSortHelper(A, mid+1, high)
        arrayMergeInPlace(A, low, mid, high)

# Algorithm 12.7: In-place array merge. 309
def arrayMergeInPlace(A, low, mid, high):
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
        elif C[i] <= C[j]:
            A[k] = C[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1


# Algorithm 12.9: Quicksort. 318 ---------------------------------------------------
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
    p = random.randint(low, high)
    A[p], A[high] = A[high], A[p]
    b = low
    for i in range(low, high):
        if A[i] < A[high]:
            A[i], A[b] = A[b], A[i]
            b += 1
    A[high], A[b] = A[b], A[high]
    return b


# LISTS -----------------------------------------------------------------------------
functions = [selectionSort,   #0
             selectionSortCE, #1
             insertionSort,   #2
             heapSort,        #3
             mergeSort,       #4
             quickSort]       #5

fxns = len(functions)
run_times = [None]
all_run_times = [[None] for i in range(fxns)]


# MAIN FUNCTIONS -----------------------------------------------------------------------

# Takes an array A, a function number f, and a list of run times rt.
def functionHandler(A, f, rt):
    fn = functions[f].__name__
    # Calculate the function's run time:
    start_time = time.thread_time()
    functions[f](A)
    run_time = time.thread_time() - start_time
    # print("%s: %s seconds" % (fn, run_time))

    if loLists(rt): #If rt is a list of lists:
        if rt[f][0] == None:
            rt[f][0] = fn
            rt[f].append(run_time)
        else:
            rt[f].append(run_time)
    else: #If rt is only a single list:
        if rt[0] == None:
            rt[0] = fn
            rt.append(run_time)
        else:
            rt.append(run_time)

# Returns true if lol is a list of lists.
def loLists(lol):
    if any(isinstance(el, list) for el in lol):
        return True

# runs a function f (or all functions if f=None) n times on a list 10^e long.
def getTimes(f, n, e):
    all_fxns = False
    if e >= 10:
        nums = [i for i in range(e)]
    elif e < 10:
        nums = [i for i in range(10 ** e)] #Generate a number list 10^e long.
    # Run the function n times:
    for i in range(n):
        random.shuffle(nums) #Shuffle the list to randomize the order.
        # If f is None, run all functions in the fxn list through the handler:
        if f == None:
            for j in range(fxns): #Iterates through each fxn in the handler:
                array = copy.deepcopy(nums) #Keeps the list random for each fxn.
                functionHandler(array, j, all_run_times)
            all_fxns = True
        else:
            functionHandler(nums, f, run_times)
    # Determine whether to retun a list of lists or just a list:
    if all_fxns == True:
        return all_run_times
    else:
        return run_times

# Takes the return value of getTimes() and returns the average run time.
def getAverageTime(times):
    time_data = []
    if not loLists(times):
        sum = 0
        c = 0
        avg = 0
        for i in times:
            if i != times[0]: #times[0] is the function name.
                sum += i
                c += 1
        avg = sum / c
        time_data.append(times[0])
        time_data.append("Avg: %s" % (avg))
    else:
        for i in range(len(times)):
            sum = 0
            c = 0
            avg = 0
            for j in times[i]:
                if j != times[i][0]:
                    sum += j
                    c += 1
            avg = sum / c
            time_data.append([times[i][0]])
            time_data[i].append("Avg: %s" % (avg))
    return time_data

# Returns a list the average times of function f on a list 10^1 to 10^e long.
def speedTester(f, n, e):
    speed_tester = []
    for i in range(1, e+1):
        time_data = getAverageTime(getTimes(f, n, i))
        speed_tester.append("%s - Length 10^%s - %s" % (time_data[0], i, time_data.pop()))
        print(speed_tester[i-1])
    return speed_tester

# print(getAverageTime(getTimes(2, 10000, 25)))
# print(getAverageTime(getTimes(5, 10000, 50)))

# speedTester(2, 1000, 2)
speedTester(5, 100, 5)

# quickSort - Length 10^1 - Avg: 0.0
# quickSort - Length 10^2 - Avg: 0.0
# quickSort - Length 10^3 - Avg: 0.0020833333333333333
# quickSort - Length 10^4 - Avg: 0.021875
# quickSort - Length 10^5 - Avg: 0.176875
# quickSort - Length 10^6 - Avg: 1.8119791666666667

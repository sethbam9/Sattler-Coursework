
# Variables
data = [5, 7, 10, 11, 4, 3, 6, 10, 1, 15, 2, 9]
Q = []
head = tail = 0
max_size = 10

def Enqueue(Q, i): #adds item i to the tail of the queue Q.
    if len(Q) <= max_size:
        Q.append(i)
    else:
        return print("Queue is full")
    # Update the tail index
    global head
    global tail
    if tail < max_size:
        tail += 1
    elif head != 0:
        tail = 0

def Dequeue(Q): #removes an item from the front (head) of the queue.
    global head
    if IsQueueEmpty(Q):
        return print("Error")
    if head < max_size:
        Q.pop(0)
        head +=1
    else:
        Q.pop(0)
        head = 0

def IsQueueEmpty(Q): #returns true if the queue Q is empty, false otherwise.
    if len(Q) == 0:
        return True
    else:
        return False

for i in data:
    Enqueue(Q, i)
for i in range(3):
    Dequeue(Q)
print(head)
print(tail)

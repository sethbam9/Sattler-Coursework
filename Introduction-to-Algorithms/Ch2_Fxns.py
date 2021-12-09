# Inspiration for the class implementation from: https://www.edureka.co/blog/linked-list-in-python/

class Node:
    def __init__(self, next_node, data):
        self.next_node = next_node = None
        self.data = data = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

class LinkedList:
    def __init__(self, head):
        self.head = head = None

# adds node n after node p in list L. If p is null, then we insert n as the new
# head of the list. The function returns a pointer to n. We assume that the node n
# has already been created with some data that we want to add in the list. We will
# not get into the details on how nodes are actually created. Brieﬂy, some memory
# must be allocated and initialized,so that the node contains the data we want and
# a pointer. InsertListNode then needs only change pointers. It must make the pointer
# of n point to the next node, or to null, if p was the last node of the list. It
# must also change the pointer of p to point to n, if p is not null.
    def InsertListNode(self, p, n):
        p = self.head
        n = Node(next_node)
        if p == None:
            self.head = next_node
        return pointer

# adds a node containing d after node p in list L. If p is null, then we insert
# the new node as the new head of the list. The function returns a pointer to the
# newly inserted node. The diﬀerence with InsertListNode is that InsertInList creates
# the node that will contain d, whereas InsertListNode takes an already created node
# and inserts it in the list. InsertListNode inserts nodes, whereas InsertInList inserts
# data contained in nodes it creates. That means that InsertInList can use
# InsertListNode to insert in the list the node it creates.
def InsertInList(self, pointer, data):
    pointer = InsertListNode()
    data = Node(data)
    if pointer == None:
        self.head = data
    return pointer

# removes node r from the list and returns that node; p points to the node preceding r
# in the list, or null if r is the head. We will see that we need to know p in order
# to remove the item pointed by r eﬃciently. If r is not in the list, it returns null.
def RemoveListNode(self, node):
    pointer = None
    node = self.node
    index = self.head
    while index =! None:
        if index == node:
            self.pointer = self.node
        elif index == None
        else:
            pointer = index
        if


# removes the ﬁrst node containing d from the list and returns the node. The diﬀerence
# with RemoveListNode is that it will search the list for the node containing d, ﬁnd it,
# and remove it; d does not point to the node itself; it is the data contained inside
# the node. If there is no node containing d in the list, RemoveFromList returns null.
def RemoveFromList(self, data):
    index = self.head
    data = self.data
    while index != None:
        if index == data:
            self.pointer = self.node
        elif index == None:
            return None
        index = self.node

# returns the node following p in list L. If p is the last node in the list, then it
# returns null. If p is null, then it returns the ﬁrst node of L, the head. The
# returned node is not removed from the list.
def GetNextListNode(L,p):
    if p == None:
        return L[0]
    elif L[-1] == p:
        return None
    else:
        return L[1]

# searches the list L for the ﬁrst node containing d. It returns the node, or null
# if no such node exists; the node is not removed from the list.
def SearchInList(L,d):
    return d

a = 5
b = 10
c = 1
d = 2
L = CreateList()

i = 0
while i < 7:
    if i == 0:
        print(L)
        i += 1
    if i == 1:
        InsertListNode(L,a,b)
        print(L)
        i += 1
    if i == 2:
        InsertInList(L,c,d)
        print(L)
        i += 1
    if i == 3:
        RemoveListNode(L,c,d)
        print(L)
        i += 1
    if i == 4:
        RemoveFromList(L,a)
        print(L)
        i += 1
    if i == 5:
        GetNextListNode(L,b)
        print(L)
        i += 1
    if i == 6:
        break

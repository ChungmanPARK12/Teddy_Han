import time

# list
lists = []
file = open("products.txt")
start_time = time.perf_counter()
for line in file:
    lists.append(line)
end_time = time.perf_counter()

# calculation run time
runTime = (end_time - start_time)
# conversion of mileseconds
milliseconds_time = runTime * 1000
print("list took", milliseconds_time, "milliseconds")

# stack
stack = []
file = open("products.txt")
start_time = time.perf_counter()
for line in file:
    stack.append(line)
end_time = time.perf_counter()

# calculation run time
runTime = (end_time - start_time)
# conversion of mileseconds
milliseconds_time = runTime * 1000
print("stack took", milliseconds_time, "milliseconds")

# queue
queue = []
file = open("products.txt")
start_time = time.perf_counter()
for line in file:
    queue.append(line)
end_time = time.perf_counter()

# calculation run time
runTime = (end_time - start_time)
# conversion of mileseconds
milliseconds_time = runTime * 1000
print("queue  took", milliseconds_time, "milliseconds")

# Sets
setz = set()
file = open("products.txt")
start_time = time.perf_counter()
for line in file:
    setz.add(line)
end_time = time.perf_counter()

# calculation run time
runTime = (end_time - start_time)
# conversion of mileseconds
milliseconds_time = runTime * 1000
print("To use the set it took", milliseconds_time, "milliseconds")


# linked list
class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create Empty Linked List
l_list = LinkedList()

# open File
file = open("products.txt")
current_node = None

# get start time
start_time_ll = time.perf_counter()
for line in file:
    # create a new node & give the new node data (the line we are reading)
    node = Node(line)

    # Checking for an empty head and assigning it
    if l_list.head is None:
        # make sure current_node is not set to None when the loop starts
        current_node = node
        l_list.head = node

    # link the node we are current on (current_node) to the new node we just created
    current_node.next = node

    # assign current_node to the new node we just created
    current_node = node
# Get end time
end_time = time.perf_counter()

# calculation run time
runTime = (end_time - start_time)

# conversion of mileseconds
milliseconds_time = runTime * 1000

print("search took", milliseconds_time, "milliseconds")


def sequentialSearch(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i

    return -1


def seqSearch(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return mid


""" Test Search Setup """
NUMBER_OF_ELEMENTS = 5000
ITEM_LOCATION = 450
testList1 = list(range(NUMBER_OF_ELEMENTS))
testList2 = list(range(NUMBER_OF_ELEMENTS))

"""Test Sequential Search"""
startTime = time.perf_counter()
seqSearch(testList2, 450)
endTime = time.perf_counter()
runTime = (endTime - startTime)
print("What was the linear test runtime?")
print("RunTime was ", runTime)

"""Test Binary Search"""
startTime = time.perf_counter()
binary_search(testList2, 450)
endTime = time.perf_counter()
runTime = (endTime - startTime)
print("What was the binary test runtime?")
print("RunTime was ", runTime)

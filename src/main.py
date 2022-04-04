import time
import numpy as np
from queue import PriorityQueue
from node import Node
from util import *

logo()

try:
    fileName = input("Input File (Ex: 1.txt)\n> ")  
    mat = np.loadtxt("../test/" + fileName, dtype=int).flatten()
except FileNotFoundError:
    print("\nFile not found")
    input("Press ENTER to exit...")
    exit()

start = time.time()

# Inisiasi variabel
raisedNodeCount = 0
queue = PriorityQueue()
table = {}

first = Node(None, mat, 0)
node = first
table[str(node.val)] = True

print("\n-- Initial State --")
first.print()
reach = sum_kurang(node)

if (reach % 2 != 0):
    print("\nPuzzle doesn't have a solution")
    input("Press ENTER to exit...")
else:
    queue.put((first.cost, first))

    while (not queue.empty() and not node.isSolution()):
        node = queue.get()[1]
        table[str(node.val)] = True

        nodes = node.raiseChild()
        for x in nodes:
            if (str(x.val) not in table):
                queue.put((x.cost, x))
                table[str(x.val)] = True
                raisedNodeCount += 1

    step = []
    # Pake parent biar gk ribet conditional pas proses
    while (node.parent != None):
        step.append(node)
        node = node.parent

    for i in range(len(step)-1, -1, -1):
        print("\n-- Step %d: %s --" % (len(step) - i, step[i].takenMove))
        step[i].print()

    if (len(step) == 0):
        stepCount = 0
    else:
        stepCount = step[0].step
        
    print("\n-- Solution Found --")
    print("Step Taken: %d" % stepCount)
    print("Raised Node Count: %d" % raisedNodeCount)
    print("Time Taken: %f seconds" % (time.time() - start))
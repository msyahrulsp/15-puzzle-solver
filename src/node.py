import numpy as np

class Node:
    def __init__(self, parent, mtx, step, cmd=""):
        self.parent = parent
        self.val = mtx
        self.move = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.takenMove = cmd

        # remove ava move
        if (cmd == "UP"):
            self.move.remove("DOWN")
        if (cmd == "DOWN"):
            self.move.remove("UP")
        if (cmd == "LEFT"):
            self.move.remove("RIGHT")
        if (cmd == "RIGHT"):
            self.move.remove("LEFT")

        self.step = step
        self.cost = self.count() + self.step

    def findEmpty(self):
        for i in range(16):
            if self.val[i] == 16:
                return i

    def print(self):
        for i in range(16):
            if (self.val[i] == 16):
                print("   -", end="")
            else:
                print("%4d" % self.val[i], end="")
            if ((i + 1) % 4 != 0):
                print(" ", end="")
            else:
                print()

    def isSolution(self):
        solution = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    
        return (np.array_equal(self.val, solution))

    # ngitung tile yang gk sesuai, exclude empty
    def count(self):
        res = 0

        for i in range(16):
            if self.val[i] != 16 and self.val[i] != i+1:
                res += 1

        return res

    # for raisechild purposes
    def copy(self):
        return np.array(self.val[:])

    # buat prioqueue
    def __lt__(self, other):
        return self.cost < other.cost

    def raiseChild(self):
        res = []
        idx = self.findEmpty()

        for move in self.move:
            arr = self.copy()
            if move == "UP":
                if (idx // 4) - 1 >= 0:
                    temp = arr[idx - 4]
                    arr[idx - 4] = arr[idx]
                    arr[idx] = temp
            if move == "DOWN":
                if (idx // 4) + 1 <= 3:
                    temp = arr[idx + 4]
                    arr[idx + 4] = arr[idx]
                    arr[idx] = temp
            if move == "LEFT":
                if (idx % 4) - 1 >= 0:
                    temp = arr[idx - 1]
                    arr[idx - 1] = arr[idx]
                    arr[idx] = temp
            if move == "RIGHT":
                if (idx % 4) + 1 <= 3:
                    temp = arr[idx + 1]
                    arr[idx + 1] = arr[idx]
                    arr[idx] = temp
            res.append(Node(self, arr, self.step + 1, move))

        return res
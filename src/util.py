import numpy as np

# get kurang
def kurang(mat):
    res = [0 for i in range(16)]
    print("\n-- Reachable Goal --")
    for i in range(16):
        for j in range(i+1, 16):
            if mat.val[i] > mat.val[j]:
                res[mat.val[i]-1] += 1
        print("Kurang(%d) = %d" % (mat.val[i], res[mat.val[i]-1]))

    return res

# get sumkurang sama x
def sum_kurang(mat):
    sumRes = sum(kurang(mat))
    idx = mat.findEmpty()

    if ((idx // 4 + idx % 4) % 2 == 0):
        X = 0
    else:
        X = 1

    print("Sum Kurang(i) + X = %d" % (sumRes + X))
    return (sumRes + X)

def logo():
    print("  _ ____        ____                _      ")
    print(" / | ___|      |  _ \\ _   _ _______| | ___ ")
    print(" | |___ \\ _____| |_) | | | |_  /_  / |/ _ \\")
    print(" | |___) |_____|  __/| |_| |/ / / /| |  __/")
    print(" |_|____/      |_|    \__,_/___/___|_|\___|\n")
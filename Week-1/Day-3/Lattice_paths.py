import math
def pathCounter(gridSize):
    p = math.factorial(gridSize*2) // (math.factorial(gridSize)**2)
    return p
    
t = int(input())
for _ in range(0,t):
    size = int(input())
    n = pathCounter(size)
    print("Routes: %d" % (n))
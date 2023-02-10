def solve(numheads, numlegs):
    b = True
    for i in range(numheads+1):
        j = numheads - i
        if j*4 + i*2 == numlegs:
            print(i, j)
            b = False
    if b:
        print("No")

x, y = tuple(map(int, input().split()))    
solve(x, y)

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True 

newlist = [x for x in range(100) if prime(x)]

print(newlist)
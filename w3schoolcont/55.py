# def myfunc(n):
#   return abs(n - 50)

def func_1(x):
    if x > 0:
        return True
    else:
        return False

thislist = [-1, 100, 50, 65, 82, 23, -3, -2]
thislist.sort(key = func_1)
print(thislist)
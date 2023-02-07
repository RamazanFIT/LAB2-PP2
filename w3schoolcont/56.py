def myfunc(n):
  return abs(n - 50)
    # if n > 23:
    #     return True
    # else:
    #     return False

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
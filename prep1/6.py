q = int(input())
cnt = 0
for i in range(1, q) : 
    flag = bool(True)
    cnt+=1
    for s in range(2, i) :
        if i % s == 0 :
            flag = False 
    if flag : 
        print(i, end = " ")
    if(cnt % 10 == 0) : print()

        
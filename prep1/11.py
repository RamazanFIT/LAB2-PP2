q = int(input())
cnt = 0
for i in range(q) :
    a = int(input())
    last = 1
    # a //= 10 
    while(a != 0) : 
        if a % 10 == last : cnt+=1
        a //= 10
    
print(cnt)
        
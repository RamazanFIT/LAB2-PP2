q = int(input())
cnt = 0 

a = int(q % 10)
q //= 10 
while(q != 0) :
    if(q % 10 == a) : cnt+=1
    q //= 10
print(cnt+1)


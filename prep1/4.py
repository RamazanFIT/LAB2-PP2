q = int(input())
cnt = 0
for i in range(1, int(pow(q, 0.5))+1) :
    if(q % i == 0) : cnt+=1

print(cnt*2-1)
cnt = 1
q = int(input())
w[q][q]
cnt1 = 0

while(cnt != q*q + 1) :
    for i in range(cnt1, q-cnt1) :
        w[cnt1][i] = cnt
        cnt+=1
    
    for i in range(cnt1+1, q-cnt1) : 
        w[i][q-1-cnt1] = cnt 
        cnt+=1
    for i in range(q-2-cnt1, cnt1, -1) :
        w[q-1-cnt1][i] = cnt 
        cnt+=1
    for i in range(q-2-cnt1, cnt1+1, -1) :
        w[i][cnt1] = cnt 
        cnt+=1
    cnt1+=1

for i in range(0, q) :
    for s in range(0, q) :
        print(w[i][s], sep =" ")
    
    print()
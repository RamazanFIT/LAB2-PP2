q = int(input())

# while(True) :
#     if(q % 2 == 0) : q/=2
#     elif q == 1 : print("YES"), exit()
#     elif q == 0 : print("NO"), exit()
#     else : print("NO"), exit()
k = 1 

while(k < q) :
    k*=2
# print(k)
if(k == q) : 
    print("YES")
else : 
    print("NO")

q = int(input())
a= int(input())
cnt = 0
flag = bool(True)
while a != 0 :
    if(q == a and flag) : cnt+=1
    else : flag = False 
    a = int(input())
print(cnt+1)
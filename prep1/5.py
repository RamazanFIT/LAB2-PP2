x = int(input())
y = int(input())
z = int(input())
cnt = 0
while (x != 0 and y != 0 and z != 0) :
    if(y > x and y > z) : cnt+=1
    x, y = y, z 
    z = int(input())
print(cnt)


a = 1 
b = 1
q = int(input())
global up
global down
if q == 1 : print(1, "/", 1, sep=""), exit()
for i in range (q-1) :
    up = int(a + b )
    down = int(a) 
    a, b = a + b, a 

print(up, "/", down, sep="")
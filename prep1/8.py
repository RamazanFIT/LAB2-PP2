# # while(q = int(input()) != 0) :

# q = int(input())
# k = int(q)
# while(q != 0) :
#     k = min(q, k)
#     q = int(input())

# print(k)

    
q = int(input())
k = 0
cnt = 0
c = int(q)
a = int(input())
while(a != 0) :
    # a = int(input())
    cnt+=1
    if a <= q : k = cnt 

        
    c = min(a, c)
    a = int(input())

print(k, c, sep = "  ")
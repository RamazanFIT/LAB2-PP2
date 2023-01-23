# q = int(input())

# size = 0
# a = int(q) 
# while(a != 0) :
#     size+=1
#     a//=10
#     # print(a, size)

# # print(q//((size-1)*10))
# print(q // (pow(10, size-1)))
q = int(input())

while q > 9 : 
    q //= 10 
print(q)
# # q = int(input())

# # a = int(input())
# # c = int(q)
# # d = int(q)
# # while(a != 0) :
# #     c = min(c, a)
# #     if(a < c) : d
# # q = int(input())
# # c = int(q)
# # d = int(c)


# # while(q != 0) :
# #     c = min(c, q)
# #     if(q < c) : 

# q = int(input())

# a = int(input())
# k = int(min(a, q)) 
# d = int(max(q, a))
# while(a != 0) :
#     k = min(k, a)
#     if(a > k) : d = min(a, d)
#     a = int(input())

# print(k, d)

# q = int(input())
# a = int(input())
# min1 = int(min(q, a))
# min2 = int(max(q, a))

# while a != 0 :
   
#     if(a < min1) : min1, min2 = a, min1
#     else : min2 = min(min2, a)
#     a = int(input())

# print(min1, min2, sep="  ")

q = int(input())
min1 = abs(q*2)
min2 = abs(q + 1)
while(q != 0) :
    if(q < min1) : min1, min2 = q, min1 
    elif q < min2 : min2 = q 
    q = int(input())
    
    

print(min1, min2, sep = "  ")

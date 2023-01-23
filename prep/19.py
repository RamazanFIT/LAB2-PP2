q = int(input())
a = 0
b = 1
if q == 0 :
    print(0)
    exit()
elif q == 1 : 
    print(1)
    exit()
        
for i in range(0, q-2) :
    # c = a
    # a = b 
    # b+=c
    # a, b = b, a + b 
    b, a = a + b, b

print(b)
# 0 1 1 2 3 5 8 13

# for i in range(q) :
#     print("HI ROMA")
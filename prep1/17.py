# def hello_n(name: str, n : int):
#     for i in range(n):
#         print('Privet', name)


# hello_n('VASYA', 4)

# hello_n('PETYA', 2)

# vasya = "vauuuuu", 10

# hello_n(* vasya)
# //////////////////////////////////////////////////////////////
# def hello_n(name, n ):
#     for i in range(n):
#         print('Privet', name)


# hello_n('VASYA', 4)

# hello_n('PETYA', 2)

# vasya = "vu", 10

# hello_n(* vasya)

# A = range(1, 20, 2)
# B = 1, 2, 3, 4 #нельзя изменить картеж

# print(*A)

# print(A)

# B[2] = 7

# print(B)

# V = [1, 2, 3, 4] # list

# v.append(1000)

# V[2] = 10

# print(*V)

# C = "ko", "ro" , "do", "ki"

# N = enumerate(C)


# print(*N)


# V = [1, 2, 3, 4, 5]

# V.append(10) only one argument we can add to list
# print(*V)
# .
# .
# ....
# .
# .
# .

# Множества и словари

# множнства - set  only unique elements

# словари - dict values of key not unique but keys have to be unique elements

# S = {1, 2, 3, 4, 5} SET - очень быстро ищет элемент из множества

# S.add(6)

# if 4 in S:
#     print("FUCK")
# else :
#     print("HI")

# if 7 in S:
#     print("HELLO")
# else :
#     print("FUCK YOU")

# for i in S:
#     print(i, "!")


# dictionarry

# D ={"A" : 123, "B" : 100, "C" : 130, "D" : 124}

# print(*D)

# print(D["A"])\

# D["SALAM"] = 777

# print(D["SALAM"])
# print((D.keys()))
# print(D)
# print(*D)

# for key in D:
#     print(key, end=" ")
#     print(D[key])


# /
# /
# /
# /
# //

# /
# /
# /


# function

# Rabota function : 1 local -> 2 enclosed -> 3 global -> 4 Built in(main) ;

# def foo():
#     pass 
#     return 

# def foo() -> int :

# def foo(x : int) :
#     return x**2

# y = foo(2)

# print(y)


# def foo(X, y):
#     X[0] = 7
#     X[1] = "Roma"
#     X = [1, 1, 1]
#     # y = 1

# A = [1, 2, 3]

# y = 8

# foo(A, y)

# print(*A, y, sep = "  ")

# переменные указывают на обекты
# def foo(x, y, z):
#     return(x*100+y*10+z)

# print(foo(1, 2, 3))

# print(foo(x = 3, y = 2, z = 1))


# def foo1(x, y, z=0):
#     return(x*100+y*10+z)

# print(foo1(1, 2, 3))

# def foo(*A, name_q):
#     for i in A:
#         print(name_q, '=', i)

# G = [1, 2, 3, 4]

# foo(*G, name_q = "roma")


# square = lambda n, g : (n+g)**2 

# for i in arr :
#     # arr[i] = square(arr[i], 1)
#     arr1 += [square(i, 1)]

# square = lambda roma: (roma)

# k = input()



# print(square(k))


# massive = input()

# massive.split(" ")

# print(*massive)

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


# num1 = [1, 2, 3, 4]

# num2 = [5, 6, 7, 1]

# func = map(lambda x, y: 2*x + y, num2, num1)
# func = list(func)
# print(func)

# l = ['sat', 'bat', 'cat', 'mat']

# arr = list(map(list, l))

# print(arr)

# l = ["1", "2", "3", "4", "5", "6"]

# arr = list(map(list, l))
# arr[0].append(100)
# print(arr)





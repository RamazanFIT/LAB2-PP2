q = int(input())

# a = int(input())
a = int(q//1000 * 10 + q // 100 % 10)
b = int(q % 100 // 10 + q % 10 * 10)

# print(a, b)
print(a - b + 1)


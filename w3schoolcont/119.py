x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
x.symmetric_difference_update(y)
g = x.symmetric_difference(y)
print(g)
print(x)
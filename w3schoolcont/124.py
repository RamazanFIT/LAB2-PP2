set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {1, 2, 3}
set_2 = set(set_1)
set_2.add(77)
print(set_1)
set_3 = {1, 2, 3, 10, 12, 13}

print(set_3.issuperset(set_1))
print(set_1.issuperset(set_2))

# CONTAINER.issuperset(вещь, которую хотим проверить)
# that is opposite to function comp.issubset(container)
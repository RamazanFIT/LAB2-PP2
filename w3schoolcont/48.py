fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

list_1 = [x.upper() for x in fruits if x[0] != 'a']
# list_1 = [x for x in fruits]
# list_1 = [x.upper() for x in list_1]
print(list_1)
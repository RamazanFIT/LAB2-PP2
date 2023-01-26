size_list = int(input())
list_1 = list()
for i in range(size_list):
    list_1.append(int(input()))


def histogram(list_1: list):
    list_2 = list()
    for i in list_1:
        list_2.append("*" * i)
    for i in list_2:
        for s in i:
            print(s, end="")
        print()

histogram(list_1)
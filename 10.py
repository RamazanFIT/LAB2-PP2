list_1 = list()
k = int(input())
for i in range(k):
    list_1.append(int(input()))

def set_1(list_1: list):
    list_1.sort()
    list_1.append("ROMA")
    list_2 = list()
    for i in range(len(list_1)-1):
        boolka = True 
        if(list_1[i] == list_1[i+1]):
            boolka = False 
        else:
            list_2.append(list_1[i])
    return list_2


print(*set_1(list_1))
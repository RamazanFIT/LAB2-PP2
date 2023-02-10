def Ispol(str_1):
    if str_1 == str_1[::-1]:
        return True 
    else:
        return False

str_1 = str(input())

print(Ispol(str_1))

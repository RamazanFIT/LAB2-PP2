from itertools import permutations

string_input = str(input())

def permut_of_str(string: str):
    string = list(permutations(string))
    list_1 = []
    for i in string:
        s = ""
        for j in i:
            s += j 
        list_1.append(s)
    return list_1 

print(*permut_of_str(string_input))

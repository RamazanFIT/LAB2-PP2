from itertools import permutations

string_input = str(input())

def permut_of_str(string: str):
    string = list(permutations(string))
    return string 

print(*permut_of_str(string_input))
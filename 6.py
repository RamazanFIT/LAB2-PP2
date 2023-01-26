string_input = input()

string_input = list(string_input.split(" "))

def reversed(list_1: list):
    list_1.reverse()
    return(list_1)

print(*reversed(string_input))
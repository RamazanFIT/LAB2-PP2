list_input = list(map(int, input().split()))

def has_33(list_input: list):
    list_string = str()
    for i in list_input:
        list_string += str(i)
    if "33" in list_string:
        return True 
    else:
        return False 

print(has_33(list_input))

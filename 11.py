string = str(input())
def ispolindrome(string: str):
    string_list = list(string)
    string_list.reverse()
    prob_string = str()
    for i in string_list:
        prob_string += i 
    if prob_string == string:
        return True 
    else:
        return False 

if ispolindrome(string):
    print("YES")
else:
    print("NO")
